from django import forms
from django.core.exceptions import ValidationError

from ..home.models import *

class MealForm(forms.Form):
    live_date = forms.DateField(
        required = True,
        label = "Date of Meal"
    )

    main_dish = forms.ChoiceField(
        required = True,
        choices = Main_Dish.objects.all().order_by('display_name'),
        label = "Entree"
    )

    side_dish = forms.MultipleChoiceField(
        required = False,
        choices = Side_Dish.objects.all().order_by('display_name'),
        label = "Side Dish(es)"
    )

class DishForm(forms.Form):
    dish_type = forms.ChoiceField(
        required = True,
        choices = [('main','Main'),('side', 'Side')],
        widget = forms.RadioSelect()
    )

    display_name = forms.CharField(
        required = True,
        label = "Name"
    )

    price = forms.DecimalField(
        required = True,
        decimal_places = 2
    )

    ingredients = forms.MultipleChoiceField(
        required = True,
        choices = Ingredient.objects.all().order_by('display_name'),
    )

    categories = forms.CharField(
        required = False,
        max_length=300,
        widget = forms.Textarea()
    )

    image = forms.FileField(
        required = False,
    )
