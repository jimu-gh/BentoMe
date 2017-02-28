from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm

from .models import User

import stripe
# Create your views here.
def index(request):
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

            print user
            # try:
            #     user.save()
            # except IntegrityError:
            #     form.addError(user.email + ' is already a member')
            # else:
            #     request.session['user'] = {
            #         'id': user.id,
            #         'first_name': user.first_name
            #     }
            #     return redirect(reverse('home:index'))
        for error in form.errors:
            messages.error(request, form.errors[error])

        print form['stripe_token']

        return redirect(reverse('users:index'))

def login(request):
    pass
