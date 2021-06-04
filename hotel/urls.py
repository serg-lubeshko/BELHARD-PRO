from django.urls import path
from hotel.views import *




urlpatterns = [
    path('', ShowRooms, name="home"),
    path('detail/<int:room_id>/', detailRooms, name="detail"),
    path('room/admin', showbooking, name = 'showbooking'),
    path('room/booking/<int:room_id>/', booking, name="booking"),
    path('room/booking/delete/<int:reservation_id>/', destroybooking, name='delete'),
    path('room/booking/confirm/<int:reservation_id>/', confirmbooking, name='ok'),
    path('service/', service, name ='service' ),


    # path('1/', show_service_statistics, name ='statics' )
]
