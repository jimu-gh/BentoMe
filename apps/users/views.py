from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm

from .models import *
from ..home.models import *

import stripe, datetime
# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect(reverse('home:dashboard'))

    context = {
        'register': RegisterForm(),
        'login': LoginForm()
    }

    return render(request, 'users/index.html', context)

def register(request):
    user = None
    if request.method == "POST":
        if 'agreement' not in request.POST:
            messages.error(request, "You must agree to the Terms of Service")
            return redirect(reverse('users:index'))
        else:
            form = RegisterForm(request.POST)
            if form.is_valid():

                print form.cleaned_data['stripe_token']

                customer = stripe.Customer.create(
                    description = form.cleaned_data['email'],
                    email = form.cleaned_data['email'],
                    card = form.cleaned_data['stripe_token'],
                )

                user = User(
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    email = form.cleaned_data['email'],
                    last_4_digits = form.cleaned_data['last_4_digits'],
                    stripe_id = customer.id
                )
                user.set_password(form.cleaned_data['password1'])

                try:
                    user.save()
                except IntegrityError:
                    form.addError(user.email + ' is already a member')
                else:
                    request.session['user'] = {
                        'id': user.id,
                        'first_name': user.first_name
                    }
                    messages.success(request, "Thanks for registering!")
                    return redirect(reverse('home:dashboard'))
            for error in form.errors:
                messages.error(request, form.errors[error])

            return redirect(reverse('users:index'))

def login(request):
    if request.method == "POST":
        response = User.objects.login(request.POST)
        if type(response) is list:
            for error in response:
                messages.error(request, error)
            return redirect(reverse('users:index'))
        else:
            request.session['user'] = {
                'id': response.id,
                'first_name': response.first_name
            }
            return redirect(reverse('home:dashboard'))

def logout(request):
    if 'user' in request.session:
        request.session.pop('user')
    return redirect(reverse('home:index'))

def show_user(request, user_id):
    if 'user' not in request.session:
        return redirect(reverse('users:index'))
    user=User.objects.get(id=request.session['user']['id'])
    print user.admin
    if int(request.session['user']['id']) != int(user_id) and user.admin != True:
        messages.error(request, "Cannot access another user's information")
        return redirect(reverse('home:dashboard'))
    today = datetime.datetime.now().date()

    user_orders = Meal.objects.filter(meal_orders__user__id=user_id).order_by('-live_date')
    past_orders = Meal.objects.filter(meal_orders__user__id=user_id, live_date__lt=today)

    context = {
        'user':user,
        'current_orders': user_orders.filter(live_date__gte=today),
        'past_orders': [{'meal': meal, 'rating': meal.meal_ratings.filter(user__id=user_id)} for meal in past_orders]
    }

    return render(request, 'users/show.html', context)

def show_order(request, meal_id):
    if 'user' not in request.session:
        return redirect(reverse('users:index'))
    this_meal = Meal.objects.get(id=meal_id)
    this_meal_users = User.objects.filter(user_orders__meal=this_meal)
    for user in this_meal_users:
        if request.session['user']['id'] == user.id:
            this_meal_user = user
            specific_messages = Message.objects.filter(user=this_meal_user) | Message.objects.filter(user=24)
            this_meal_messages = specific_messages.filter(meal=this_meal).order_by('-created_at')
        elif request.session['user']['id'] == 24:
            this_meal_user=User.objects.get(id=24)
            this_meal_messages = Message.objects.filter(meal=this_meal).order_by('-created_at')
    if int(request.session['user']['id']) != int(this_meal_user.id):
        messages.error(request, "Cannot access another user's information")
        print int(request.session['user']['id']) ==  int(user_id)
        return redirect(reverse('users:show_user',kwargs={'user_id':request.session['user']['id']}))

    context={
        'user': this_meal_user,
        'meal': this_meal,
        'messages': this_meal_messages
    }
    return render(request, 'users/order.html', context)

def edit_card(request):
    if 'user' not in request.session:
        return redirect(reverse('users:index'))

    if request.method == "POST":
        customer = User.objects.get(id=request.session['user']['id'])

        customer.card = request.POST['stripe_token']

        customer.save()

        return redirect(reverse('home:dashboard'))

def create_feedback(request):
    if request.method == "POST":
        message = request.POST['message']
        meal_id = request.POST['meal_id']
        try:
            this_meal = Meal.objects.get(id=meal_id)
            this_user = User.objects.get(id=request.session['user']['id'])
            this_order = Meal_Order.objects.filter(meal=this_meal,user=this_user)
            for order in this_order.all():
                this_order = order
            print this_order.id
            Message.objects.create(user=this_user,message=message,meal=this_meal)
            messages.success(request, "Thank you for your feedback!")
        except:
            messages.error(request, "Cannot have feedback for this meal")
        return redirect(reverse('users:show_order',kwargs={'meal_id':this_meal.id}))
