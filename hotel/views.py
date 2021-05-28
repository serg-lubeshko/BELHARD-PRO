from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render


from hotel.forms import BookingForm, ServiceHotelForm
from hotel.models import Room, Facilities, BokkingRoom, TypeService, ServiceHotel


def ShowRooms(request):
    rooms = Room.objects.order_by("title")
    context = {"rooms": rooms}
    return render(request, template_name="hotel/index.html", context=context)


def detailRooms(request, room_id):
    detail = Room.objects.get(id=room_id)
    facilit = detail.facilities.all()
    context = {"detail": detail, "facilitie": facilit}
    return render(request, template_name="hotel/detailroom.html", context=context)


def check_date(room_booking, date_arrival,date_departure):
    for dates in room_booking:
        date_1 = str(dates[0])
        # print(date_1, 'date1')
        date_2 = str(dates[1])
        # print(type(date_arrival),'hhhhhhhhhhhhhhhhhhh')
        if date_arrival > date_2:
            return True
        elif date_departure < date_1:
            return True
        elif date_1<=date_arrival <= date_2:
            return False
        else:
            return False
        # print(date_1, 'date_1')
        # print(date_2, 'date_2')


def booking(request, room_id):
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
                note.save()
                messages.success(request, "Номер забронирован")

    else:
        form = BookingForm()
    context = {"form": form, "room": room}
    return render(request, template_name="hotel/booking.html", context=context)

def service(request):
    serv = TypeService.objects.all()
    len_serv = len(serv)
    form = ServiceHotelForm()
    form = ServiceHotelForm()
    if request.method == "POST":
        user = request.user.id
        ServiceHotel.objects.filter(users_id=user).delete()
        for item in range(1,len_serv+1):
            dictmodel = {}
            ServiceHotel.objects.filter(users_id=user).update(**dictmodel)
            mark = request.POST[str(item)]
            dictmodel["mark"] = int(mark)
            dictmodel["type_id"] = item
            dictmodel["users_id"] = user
            ServiceHotel.objects.create(**dictmodel)
        messages.success(request,"Спасибо за Вашу оценку!")
        # if ServiceHotel.objects.filter(users_id=user):
        #     print("efwefwee")
        #     A= ServiceHotel.objects.filter(type_id=item, users_id=user).update(**dictmodel)
        #     print(A,"fwefwe")
        # else:
        #     print("aaa")
        #     ServiceHotel.objects.create(**dictmodel)




            # ServiceHotel.objects.update_or_create(type_id=user, defaults=dictmodel)




    return render(request, 'hotel/service.html', context={ 'services':serv})