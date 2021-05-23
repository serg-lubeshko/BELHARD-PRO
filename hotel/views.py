from django.shortcuts import render

from hotel.models import Room


def ShowRooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "hotel/index.html", context=context)

def DetailRooms(request, room_id):
    detail = Room.objects.get(id=room_id)
    context = {"rooms": detail}
    return render(request, "hotel/detailroom.html", context=context)