from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.forms import RegisterForms

def register(request):
    if request.method == "POST":
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Поздравляем! Регистрация прошла успешно.")
            # return redirect("home")
        else:
            messages.error(request, "Ошибка регистрации!")
            # form = UserCreationForm()
    else:
        form = RegisterForms()
    context = {"form": form}
    return render(request, template_name='user/register.html', context=context)


def login(request):
    return render(request, template_name='user/login.html')
