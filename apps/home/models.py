from __future__ import unicode_literals

from django.db import models
from ..users.models import User

# Create your models here.
class Meal(models.Model):
    live_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Side_Dish(models.Model):
    name = models.CharField(max_length=100)
    meal = models.ManyToManyField(Meal, related_name="side_dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="side_dishes")
    categories = models.ManyToManyField(Category, related_name="side_dishes")
    image = models.FileField(upload_to='')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Main_Dish(models.Model):
    name = models.CharField(max_length=100)
    meal = models.ManyToManyField(Meal, related_name="main_dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="main_dishes")
    categories = models.ManyToManyField(Category, related_name="main_dishes")
    image = models.FileField(upload_to='')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meal_Order(models.Model):
    user = models.ForeignKey(User, related_name="user_orders")
    meal = models.ForeignKey(Meal, related_name="meal_orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rating(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="user_ratings")
    meal = models.ForeignKey(Meal, related_name="meal_ratings")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
