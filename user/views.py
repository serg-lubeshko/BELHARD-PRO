from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Поздравляем! Регистрация прошла успешно")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, 'user/register.html', context=context)


def login(request):
    return render(request, 'user/login.html')
