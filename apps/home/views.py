from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *
from ..users.models import *

import datetime, stripe

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def dashboard(request):
    today = datetime.date.today()
    days_left_in_week = 7 - today.isoweekday()
    end_of_week = today + datetime.timedelta(days=days_left_in_week)
    end_of_next_week = end_of_week + datetime.timedelta(days=7)

    meals_for_the_week = Meal.objects.filter(live_date__gte=today, live_date__lt=end_of_week).order_by('live_date')
    meals_for_next_week = Meal.objects.filter(live_date__gt=end_of_week, live_date__lt=end_of_next_week).order_by('live_date')

    context = {
        'this_week_meals': meals_for_the_week,
        'next_week_meals': meals_for_next_week,
        'prev_meals': Meal.objects.filter(live_date__lt=today).order_by('live_date')
    }
    for meals in meals_for_next_week:
        for side in meals.side_dishes.all():
            print side.name


    user = None

    if 'user' in request.session:
        user = User.objects.get(id=request.session['user']['id'])
        user_orders = user.user_orders.all()
        context['user_orders'] = [ order.meal.live_date for order in user_orders ]

    def place_week_meal_in_context(context, meals_for_the_week):
        for meal in meals_for_the_week:
            if meal.live_date.isoweekday() == 1:
                #monday
                context['monday'] = meal
            elif meal.live_date.isoweekday() == 2:
                #tuesday
                context['tuesday'] = meal
            elif meal.live_date.isoweekday() == 3:
                #wednesday
                context['wednesday'] = meal
            elif meal.live_date.isoweekday() == 4:
                #thursday
                context['thursday'] = meal
            elif meal.live_date.isoweekday() == 5:
                #friday
                context['friday'] = meal

    place_week_meal_in_context(context, meals_for_the_week)

    return render(request, 'home/dashboard.html', context)

def order_meal(request, meal_id):
    if 'user' not in request.session:
        return redirect(reverse('home:index'))

    if request.method == "POST":
        user = User.objects.get(id=request.session['user']['id'])

        if not user.check_password(request.POST['password']):
            messages.error(request, "Wrong password")
            return redirect(reverse('users:index'))

        print request.POST

        today = datetime.date.today()
        try:
            meal = Meal.objects.filter(live_date__gte=today).get(id=meal_id)
        except:
            messages.error(request, "Meal is not available")
            return redirect(reverse('home:dashboard'))

        num_sides = 0

        if request.POST['sides'] == '3':
            num_sides = 2
        elif request.POST['sides'] == '0':
            num_sides = 0
        else:
            num_sides = 1

        print num_sides

        total_price = 700 + (num_sides * 100)

        charge = stripe.Charge.create(
            amount=total_price,
            currency="usd",
            description="Order for: " + str(meal.live_date),
            customer=user.stripe_id,
            receipt_email=user.email
        )

        print charge

        if charge.outcome.type == 'authorized':
            Meal_Order.objects.create(
                user=user,
                meal=meal,
                sides=num_sides
            )
            messages.success(request, "Order was created successfully")
            return redirect(reverse('home:dashboard'))
        else:
            print "error"
            messages.error(request, "Order was declined for card ending in: " + user.last_4_digits)
            return redirect(reverse('home:dashboard'))
