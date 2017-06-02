from django.shortcuts import render, redirect
from django.contrib import messages
from ..home.models import *
from .forms import *
from ..users.models import *
from django.core.urlresolvers import reverse
from django.db.models import Count
import datetime, time
from django.contrib import messages
from ..users.forms import RegisterForm, LoginForm
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def login(request):
    if request.method == "POST":
        response = User.objects.login(request.POST)
        if type(response) is list:
            for errors in response:
                messages.error(request, errors)
            return redirect(reverse('adminbento:index'))
        elif User.objects.get(id=response.id).admin == True:
            print response.admin
            request.session['user'] = {
                'id': response.id,
                'first_name': response.first_name,
                'admin' : True
            }
            return redirect(reverse('adminbento:dashboard'))
        else:
            messages.error(request, "You are not an admin.")
            return redirect(reverse('users:index'))

def logout(request):
    if 'user' in request.session:
        request.session.pop('user')
    return redirect(reverse('adminbento:index'))

def dashboard(request):
    context={
        'messages' : Message.objects.filter(meal__live_date__lt=datetime.date.today()).order_by("-created_at"),
        'meals' :Meal.objects.annotate(num_sold=Count('meal_orders')).filter(live_date__lt=datetime.date.today()),
    }
    return render(request, 'adminbento/dashboard.html', context)

def add_dish(request):
    return render(request, 'adminbento/adddish.html',
    {
        'dish_form': DishForm(),
    })
    ##refrence the model creation once method is determined
    return redirect(reverse('adminbento:add_dish'))


def create_dish(request):
    if request.method == "POST":

        form = DishForm(request.POST)

        if not form.is_valid():
            messages.error(request, "Please Submit Valid information")
            return redirect(reverse('adminbento:add_dish'))

        print request.POST
        post_ingredients_ids = request.POST.getlist('ingredients')
        new_ingredients = request.POST['addingredients']
        ingredients = []

        if new_ingredients:
            new_ingredients = new_ingredients.strip().split(',')
            for i in range(len(new_ingredients)):
                new_ingredients[i] = new_ingredients[i].strip().title()

        print new_ingredients

        if type(new_ingredients) is list:
            for ingredient in new_ingredients:
                display_name = ingredient
                name = ingredient.lower().replace(" ", "_")
                try:
                    duplicate_ingredient = Ingredient.objects.get(name=name)
                    if duplicate_ingredient not in ingredients:
                        ingredients.append(duplicate_ingredient)
                except:
                    created_ingredient = Ingredient.objects.create(
                        display_name=display_name,
                        name=name
                    )
                    ingredients.append(created_ingredient)


        for ingredient_id in post_ingredients_ids:
            ingredients.append(Ingredient.objects.get(id=int(ingredient_id)))

        print ingredients

        categories = request.POST['categories']
        dish_categories = []

        if categories:
            categories = categories.strip().split("#")
            categories = filter(lambda x: x != "", categories)
            categories = map(lambda x: x.strip(), categories)
            for category in categories:
                name = str(category.lower().encode('utf-8'))
                try:
                    duplicate_category = Category.objects.get(name=name)
                    if duplicate_category not in dish_categories:
                        dish_categories.append(duplicate_category)
                except:
                    created_category = Category.objects.create(
                        name=name
                    )
                    dish_categories.append(created_category)

        image = request.FILES['image'] if 'image' in request.FILES else None

        dish_display_name = request.POST['display_name']
        name = dish_display_name.strip().lower().replace(" ", "_").replace("(", "").replace(")", "")

        if request.POST['dish_type'] == "main":
            try:
                duplicate_main_dish = Main_Dish.objects.get(name=name)
                messages.error(request, "Main Dish already exists, added ingredients and categories if they were not previously attached")
                for ingredient in ingredients:
                    duplicate_main_dish.ingredients.add(ingredient)
                for category in categories:
                    duplicate_main_dish.categories.add(category)
                if image:
                    duplicate_main_dish.image = image
                duplicate_main_dish.save()
                return redirect(reverse('adminbento:add_meal'))
            except:
                try:
                    created_main_dish = Main_Dish.objects.create(
                        display_name=dish_display_name,
                        name=name,
                        price=700,
                    )
                except:
                    messages.error(request, "Dish already created with that name")
                    return redirect(reverse('adminbento:add_dish'))
                for ingredient in ingredients:
                    created_main_dish.ingredients.add(ingredient)
                for category in dish_categories:
                    created_main_dish.categories.add(category)
                if image:
                    created_main_dish.image = image
                created_main_dish.save()
                messages.success(request, "Main Dish creation for, " + created_main_dish.display_name + " was successful")
        else:
            try:
                duplicate_side_dish = Side_Dish.objects.get(name=name)
                messages.error(request, "Side Dish already exists, added ingredients and categories if they were not previously attached")
                for ingredient in ingredients:
                    duplicate_side_dish.ingredients.add(ingredient)
                for category in dish_categories:
                    duplicate_side_dish.categories.add(category)
                if image:
                    duplicate_side_dish.image = image
                duplicate_side_dish.save()
                return redirect(reverse('adminbento:add_meal'))

                crea
            except:
                try:
                    created_side_dish = Side_Dish.objects.create(
                        display_name=dish_display_name,
                        name=name,
                        price=700,
                    )
                except:
                    messages.error(request, "Dish already created with that name")
                    return redirect(reverse('adminbento:add_dish'))
                for ingredient in ingredients:
                    created_side_dish.ingredients.add(ingredient)
                for category in dish_categories:
                    created_side_dish.categories.add(category)
                if image:
                    created_side_dish.image = image
                created_side_dish.save()
                messages.success(request, "Side Dish creation for, " + created_side_dish.display_name + " was successful")

        return redirect(reverse('adminbento:add_meal'))

def add_meal(request):
    if  'admin' not in request.session['user']:
        return redirect(reverse('adminbento:index'))

    today = datetime.date.today()

    week_length = datetime.timedelta(days=7)

    days_left_in_week = 7 - today.isoweekday()
    end_of_week = today + datetime.timedelta(days=days_left_in_week)

    start_of_next_week = end_of_week + datetime.timedelta(days=1)
    start_of_week_after_next_week = start_of_next_week + week_length

    dates_of_next_two_weeks = [[None]*5, [None]*5]

    for num in range(5):
        day = datetime.timedelta(days=num)
        dates_of_next_two_weeks[0][num] = start_of_next_week + day

    for num in range(5):
        day = datetime.timedelta(days=num)
        dates_of_next_two_weeks[1][num] = start_of_week_after_next_week + day

    context = {
        'meal_form' : MealForm(),
        'main_dish' : Main_Dish.objects.all(),
        'side_dish' : Side_Dish.objects.all(),
        'dates_of_next_two_weeks': dates_of_next_two_weeks
    }
    return render(request, 'adminbento/menu.html', context)

def create_meal(request):
    if request.method == "POST":
        meal_live_date = time.strptime(request.POST['meal_date'], "%B %d, %Y")
        entree = request.POST['main_dish']

        try:
            entree = Main_Dish.objects.get(id=int(entree))
        except:
            messages.error(request, "Main dish does not exist please try again")
            return redirect(reverse('adminbento:add_meal'))

        sides = request.POST.getlist('side_dish')

        if len(sides) > 2:
            messages.error("Can only have at most 2 side dishes")
            return redirect(reverse('adminbento:add_meal'))

        for i in range(len(sides)):
            try:
                side_dish = Side_Dish.objects.get(id=int(sides[i]))
                sides[i] = side_dish
            except:
                messages.error(request, "Side dish does not exist")
                return redirect(reverse("adminbento:add_meal"))

        meal = Meal.objects.create(
            live_date=meal_live_date,
            count=0
        )
        meal.main_dishes.add(entree)
        for side in sides:
            meal.side_dishes.add(side)
        meal.save()

        print meal
        messages.success(request, "Meal for " + str(meal.live_date) + " was created successfully")
        return redirect(reverse('adminbento:dashboard'))

def logout(request):
    if 'user' in request.session:
        request.session.pop('user')
    return redirect(reverse('home:index'))
