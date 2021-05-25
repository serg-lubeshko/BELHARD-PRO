from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from hotel.forms import BookingForm
from hotel.models import Room, Facilities, BokkingRoom


def ShowRooms(request):
    rooms = Room.objects.order_by("title")
    context = {"rooms": rooms}
    return render(request, template_name="hotel/index.html", context=context)


def DetailRooms(request, room_id):
    detail = Room.objects.get(id=room_id)
    facilit = detail.facilities.all()
    context = {"detail": detail, "facilitie": facilit}
    return render(request, template_name="hotel/detailroom.html", context=context)


def check_date(room_booking, date_arrival,date_departure):
    for dates in room_booking:
        date_1 = str(dates[0])
        print(date_1, 'date1')
        date_2 = str(dates[1])
        print(type(date_arrival),'hhhhhhhhhhhhhhhhhhh')
        if date_arrival > date_2:
            print("OK")
        elif date_departure < date_1:
            print("OK")
        else:
            return False
        # print(date_1, 'date_1')
        # print(date_2, 'date_2')


def Booking(request, room_id):
    room = Room.objects.get(id=room_id)
    # print(room_booking)
    # print(request.POST["date_arrival"], 'mmmmmm')
    # print(request.POST["date_departure"], 'mmmmmmmmmmmmmmm')
    # xx = BokkingRoom.objects.values_list("date_arrival", 'date_departure')
    # print(xx)
    # a = xx[0][0]
    # b = xx[1][1]
    # print(xx[0][0], "effeeefw")
    # print(xx[1][1], "aaaaaaaa")
    # if a > b:
    #     print('true')
    if request.method == "POST":
        room_booking = room.booking_room.values_list("date_arrival", 'date_departure')
        date_arriv = request.POST["date_arrival"]
        # print(date_arriv, "ewfwfefewfwefewfwefwefwefwe")
        date_depar = request.POST["date_departure"]
        # print(date_depar, 'wdwqdwqdwqdwqdwqdwqdwqdwdwqdwq')
        result = check_date(room_booking, date_arriv, date_depar)
        if result==False:
            messages.error(request, "Номер в указанные даты занят")
            form = BookingForm()

        else:
            form = BookingForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.users = request.user
                note.rooms = room
                # note.save()
            print(note, 'Это ноте')
    else:
        form = BookingForm()
    context = {"form": form, "room": room}
    return render(request, template_name="hotel/booking.html", context=context)
