from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



from .models import User

def validateLengthAtLeastEight(value):
    if len(value) < 8:
        raise ValidationError(
            'Password must be at least 8 characters'
        )

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        required = True,
        label = "First Name"
    )

    last_name = forms.CharField(
        required = True,
        label = "Last Name"
    )

    email = forms.EmailField(
        required = True
    )

    password1 = forms.CharField(
        required = True,
        widget = forms.PasswordInput(render_value = False),
        label = 'Password',
        min_length = 8
    )

    password2 = forms.CharField(
        required = True,
        widget = forms.PasswordInput(render_value = False),
        label = 'Password Confirmation',

    )

    last_4_digits = forms.CharField(
        required = True,
        min_length = 4,
        max_length = 4,
        widget = forms.HiddenInput()
      )

    stripe_token = forms.CharField(
        required = True,
        widget = forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
