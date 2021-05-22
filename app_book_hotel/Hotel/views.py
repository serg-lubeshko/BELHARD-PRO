from django.shortcuts import render


def showRooms(request):

    return render(request, "Hotel/index.html")


# Create your views here.
