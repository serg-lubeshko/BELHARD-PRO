from django.shortcuts import render

from hotel.models import Room, Facilities


def ShowRooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "hotel/index.html", context=context)


def DetailRooms(request, room_id):
    detail = Room.objects.get(id=room_id)
    facilit = detail.facilities.all()
    print(len(facilit))
    context = {"detail": detail, "facilitie": facilit}
    return render(request, "hotel/detailroom.html", context=context)
