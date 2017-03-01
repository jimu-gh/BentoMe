from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm

from .models import User

import stripe, datetime
# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect(reverse('meals:index'))

    context = {
        'register': RegisterForm(),
        'login': LoginForm()
    }

    return render(request, 'users/templates/index.html', context)

def register(request):
    user = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():

            print form.cleaned_data['stripe_token']

            customer = stripe.Customer.create(
                description = form.cleaned_data['email'],
                card = form.cleaned_data['stripe_token'],
            )

            user = User(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
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
                return redirect(reverse('home:index'))
        for error in form.errors:
            messages.error(request, form.errors[error])

        return redirect(reverse('users:index'))

def login(request):
    if request.method == "POST":
        response = User.objects.login(request.POST)
        if type(response) is list:
            for errors in response:
                messages.error(request, error)
            return redirect(reverse('users:index'))
        else:
            request.session['user'] = {
                'id': response.id,
                'first_name': response.first_name
            }
            return redirect(reverse('users:index'))

def logout(request):
    if 'user' in request.session:
        request.session.pop('user')

    return redirect(reverse('home:index'))

def show(request, user_id):
    if 'user' not in request.session:
        return redirect(reverse('users:index'))
    if request.session['user']['id'] != user_id:
        messages.error(request, "Cannot access another user's information")
        return redirect(reverse('home:dashboard'))

    today = datetime.datetime.now().date()

    user_orders = Meal.objects.filter(orders__user__id=user_id)

    context = {
        'user': User.objects.get(id=user_id),
        'current_orders': user_orders.filter(live_date__lte=today),
        'past_orders': [{'meal': meal, 'rating': meal.meal_rating.filter(user__id=user_id)} for meal in user_orders]
    }

    return render(request, 'show.html', context)
