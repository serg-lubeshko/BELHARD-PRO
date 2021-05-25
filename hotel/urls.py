from django.urls import path
from hotel.views import *

urlpatterns = [
    path('', ShowRooms, name="home"),
    path('detail/<int:room_id>/', DetailRooms, name="detail"),
    path('room/boking/<int:room_id>/', Booking, name="booking")
]
