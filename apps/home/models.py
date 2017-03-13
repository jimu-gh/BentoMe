from __future__ import unicode_literals

from django.db import models
from ..users.models import User


# Create your models here.
class Meal(models.Model):
    live_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.live_date)

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    display_name = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.display_name

class Side_Dish(models.Model):
    display_name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    meal = models.ManyToManyField(Meal, related_name="side_dishes", blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="side_dishes")
    categories = models.ManyToManyField(Category, related_name="side_dishes")
    image = models.FileField(upload_to='',blank=True)
    price = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.display_name

class Main_Dish(models.Model):
    display_name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    meal = models.ManyToManyField(Meal, related_name="main_dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="main_dishes")
    categories = models.ManyToManyField(Category, related_name="main_dishes")
    image = models.FileField(upload_to='',blank=True)
    price = models.IntegerField(default=700)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.display_name

class Meal_Order(models.Model):
    meal = models.ForeignKey(Meal, related_name="meal_orders")
    user = models.ForeignKey(User, related_name="user_orders")
    sides = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.first_name + " : " + str(self.meal.live_date)


class Rating(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="user_ratings")
    meal = models.ForeignKey(Meal, related_name="meal_ratings")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.first_name + " : " + str(self.meal.live_date) + " : " + str(self.rating)

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages")
    message = models.TextField(max_length=500)
    meal = models.ForeignKey(Meal, related_name="messages", blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
