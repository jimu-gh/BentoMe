from django import forms
from django.core.exceptions import ValidationError

from ..home.models import *
from ..users.models import *

class MealForm(forms.Form):
    live_date = forms.DateField(
        required = True,
        label = "Date of Meal"
    )

    main_dish = forms.ChoiceField(
        required = True,
        choices = [(entree.id, entree.display_name) for entree in Main_Dish.objects.all().order_by('display_name')],
        label = "Entree"
    )

    side_dish = forms.MultipleChoiceField(
        required = False,
        choices = [(side.id, side.display_name) for side in Side_Dish.objects.all().order_by('display_name')],
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

    ingredients = forms.MultipleChoiceField(
        required = True,
        choices = [(ingredient.id, ingredient.display_name) for ingredient in Ingredient.objects.all().order_by('display_name')],
        widget = forms.CheckboxSelectMultiple()
    )
    addingredients = forms.CharField(
        required = True,
        max_length=300,
        widget= forms.Textarea(),
        label = "Additional Ingredients"
    )
    categories = forms.CharField(
        required = False,
        max_length=300,
        widget = forms.Textarea()
    )

    image = forms.FileField(
        required = False,
    )

class IngredientForm(forms.Form):
    display_name = forms.CharField(
        required = True,
        label = "Name"
    )

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
