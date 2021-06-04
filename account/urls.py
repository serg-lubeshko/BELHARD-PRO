from django.urls import path
from account.views import *

urlpatterns = [
    path('account/', register, name="register"),     #в конспект
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout")
]
