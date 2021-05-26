from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class RegisterForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')  # порядок следования полей
        # widgets = {
        #     'username': forms.TextInput(attrs=)
        # }

        # https: // tutorial.djangogirls.org / ru / django_forms /
