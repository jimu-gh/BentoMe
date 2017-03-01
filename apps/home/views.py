from django.shortcuts import render, redirect

from .models import *

import datetime

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def dashboard(request):
    today = datetime.date.today()
    days_left_in_week = 7 - today.isoweekday()
    end_of_week = today + datetime.timedelta(days=days_left_in_week)

    meals_for_the_week = Meal.objects.filter(live_date__lte=today, live_date__gt=end_of_week).order_by('live_date')

    context = {
        'prev_meals': Meal.objects.filter(live_date__gt=today).order_by('live_date')
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

    return render(request, 'home/dashboard.html', context)
