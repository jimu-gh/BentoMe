from django.shortcuts import render, redirect

from .models import *

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
        'next_week_meals': meals_for_next_week,
        'prev_meals': Meal.objects.filter(live_date__lt=today).order_by('live_date'),
    }

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
    if 'user' not in session:
        return redirect(reverse('users:index'))

    if request.method == "POST":
        today = datetime.date.today()
        try:
            meal = Meal.objects.filter(live_date__gte=today).get(id=meal_id)
        except:
            messages.error(request, "Meal is not available to order you little shit")
            return redirect(reverse('home:dashboard'))

        user = User.objects.get(id=request.session['user']['id'])
