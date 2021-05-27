from django.contrib import admin

from hotel.models import Room, Facilities, BokkingRoom, ServiceHotel, TypeService

admin.site.register(Room)
admin.site.register(Facilities)
admin.site.register(BokkingRoom)
admin.site.register(ServiceHotel)
admin.site.register(TypeService)

# Register your models here.
