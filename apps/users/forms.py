from django import forms

from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput
        }

    confirm_pw = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = self.cleanded_data
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_pw')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
