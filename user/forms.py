from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1','password2') # порядок следования полей
        # widgets = {
        #     'username': forms.TextInput(attrs=)
        # }

        # https: // tutorial.djangogirls.org / ru / django_forms /