from django.urls import path

from .views import *

urlpatterns = [
    path("book_detail/<int:book_id>/", book_detail, name="book-detail"),
    path("", main_page),
]
