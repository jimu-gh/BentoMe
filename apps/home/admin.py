from django.contrib import admin

# Register your models here.
from .models import *

class MealAdmin(admin.ModelAdmin):
    pass
admin.site.register(Meal, MealAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class IngredientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ingredient, IngredientAdmin)

class Side_DishAdmin(admin.ModelAdmin):
    pass
admin.site.register(Side_Dish, Side_DishAdmin)

class Main_DishAdmin(admin.ModelAdmin):
    pass
admin.site.register(Main_Dish, Main_DishAdmin)

class Meal_OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Meal_Order, Meal_OrderAdmin)

class RatingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rating, RatingAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)
