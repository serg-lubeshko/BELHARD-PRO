from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from hotel.forms import BookingForm, ServiceHotelForm
from hotel.models import Room, Facilities, BokkingRoom, TypeService, ServiceHotel, Rate
from django.db.models import Count, Sum, Avg, Prefetch


def ShowRooms(request):
    query = ServiceHotel.objects.all()
    avg_score_service = (query.aggregate(score=Avg("mark"))).get('score')
    rooms = Room.objects.order_by("title")
    context = {"rooms": rooms, "score": avg_score_service}

    return render(request, template_name="hotel/index.html", context=context)


def detailRooms(request, room_id):
    detail = Room.objects.get(id=room_id)
    facilit = detail.facilities.all()
    context = {"detail": detail, "facilitie": facilit}
    return render(request, template_name="hotel/detailroom.html", context=context)


def check_date(room_booking, date_arrival, date_departure):
    for dates in room_booking:
        date_1 = str(dates[0])
        date_2 = str(dates[1])
        if date_arrival > date_departure:
            return "Date"
        if date_arrival > date_2:
            return True
        elif date_departure < date_1:
            return True
        elif date_1 <= date_arrival <= date_2:
            return False
        else:
            return False


@login_required()  # в конспект
def booking(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == "POST":
        room_booking = room.booking_room.values_list("date_arrival", 'date_departure')
        date_arriv = request.POST["date_arrival"]
        date_depar = request.POST["date_departure"]
        result = check_date(room_booking, date_arriv, date_depar)
        if result == False:
            messages.error(request, "Номер в указанные даты занят")
            form = BookingForm()
        elif result == "Date":
            messages.error(request, "Не правильно указаны даты")
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


def show_service_statistics():
    query = ServiceHotel.objects.all()
    Rate.objects.all().delete()
    list_id_type_service = set(query.values_list("type_id", flat=True))
    for item in list_id_type_service:
        stack = query.filter(type_id=item)
        avg_score_service = (stack.aggregate(score=Avg("mark"))).get('score')
        Rate.objects.update_or_create(avg_rate=avg_score_service, name_id=item)


@login_required()
def service(request):
    query = ServiceHotel.objects.all()
    serv = TypeService.objects.all()
    num_people = len(set(query.values_list("users_id", flat=True)))
    avg_score_service = (query.aggregate(score=Avg("mark"))).get('score')
    context = {'services': serv, 'num_people': num_people, 'avg_score_service': avg_score_service}
    len_serv = len(serv)
    if request.method == "POST":
        user = request.user.id
        query.filter(users_id=user).delete()
        for item in range(1, len_serv + 1):
            dictmodel = {}
            # ServiceHotel.objects.filter(users_id=account).update(**dictmodel)
            mark = request.POST[str(item)]
            dictmodel["mark"] = int(mark)
            dictmodel["type_id"] = item
            dictmodel["users_id"] = user
            ServiceHotel.objects.create(**dictmodel)
        messages.success(request, "Спасибо за Вашу оценку!")
        show_service_statistics()
        stat = Rate.objects.all()
        return render(request, 'hotel/service.html', context={**context, 'stat': stat})
    else:
        stat = Rate.objects.all()
        return render(request, 'hotel/service.html', context={**context, 'stat': stat})

def showbooking(request):
    con = BokkingRoom.objects.filter(booking=False)
    return render(request, template_name='hotel/adminbooking.html', context={'showbooking':con})