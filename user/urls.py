from django.urls import path
from user.views import *

urlpatterns = [
    path('user/', register, name="register"),     #в конспект
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
]
