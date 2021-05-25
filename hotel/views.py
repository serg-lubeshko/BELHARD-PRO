from django.http import HttpResponse
from django.shortcuts import render

from hotel.forms import BookingForm
from hotel.models import Room, Facilities


def ShowRooms(request):
    rooms = Room.objects.order_by("title")
    context = {"rooms": rooms}
    return render(request, template_name="hotel/index.html", context=context)


def DetailRooms(request, room_id):
    detail = Room.objects.get(id=room_id)
    facilit = detail.facilities.all()
    context = {"detail": detail, "facilitie": facilit}
    return render(request, template_name="hotel/detailroom.html", context=context)


def Booking(request, room_id):
    if request.method == "POST":
        form = BookingForm()
    else:
        form = BookingForm()
    room = Room.objects.get(id=room_id)
    context = {"form": form, "room":room}
    return render(request, template_name="hotel/booking.html", context=context)
