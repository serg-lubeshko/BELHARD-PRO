from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import RegisterForms, UserLoginForm
from django.contrib.auth import login, logout, authenticate


def register(request):
    if request.method == "POST":
        form = RegisterForms(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Поздравляем! Регистрация прошла успешно.")
            login(request,user)
            return redirect("home")
        else:
            messages.error(request, "Ошибка регистрации!")
            # form = UserCreationForm()
    else:
        form = RegisterForms()
    return render(request, template_name='user/register.html', context={"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request,data=request.POST)  # Параметр data= ОБЯЗАТЕЛЬНО без него не работает
        print(form, 'dw')
        if form.is_valid:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form = UserLoginForm()
    else:
        form = UserLoginForm()
    return render(request, template_name='user/login.html', context={'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')