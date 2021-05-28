from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

'''
Room
фото *
название номера *
описание *
размер номера *
курение да/нет: *       models.BooleanField(default=True)
количество людей * 
дата заезда *
дата выезда *
'''

''''
Facilities
название *
иконка*
'''

'''
Rating?
рейтинг
'''

'''''
User? кто заказывает
'''


class Room(models.Model):
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=60, verbose_name='Название номера')
    desc = models.TextField(verbose_name='Описание номера', max_length=500, blank=True)
    size = models.PositiveSmallIntegerField(verbose_name='Площадь номера')
    smoke = models.BooleanField(default=True, verbose_name='Не курят')
    # Handicapped = models.BooleanField(default=False, verbose_name='Handicapped')
    price = models.PositiveSmallIntegerField(verbose_name='Цена за сутки', default=30)
    num_people = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Кол-во спальных мест'

    )
    facilities = models.ManyToManyField("Facilities")

    # data_arrival = models.DateField(verbose_name='Дата заезда', null=True, default="")
    # data_departure = models.DateField(verbose_name='Дата отъезда', null=True, default="")
    # author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"room_id": self.pk})


class Facilities(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название удобства", unique=True)
    photo = models.ImageField(verbose_name='Иконка', upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title


class BokkingRoom(models.Model):
    date_arrival = models.DateField(verbose_name='Дата заезда')
    date_departure = models.DateField(verbose_name='Дата отъезда')
    date_order = models.DateField(auto_now_add=True, verbose_name="Дата заказа")
    desc = models.CharField(max_length=124, verbose_name='Описание')
    users = models.ForeignKey(User, related_name='booking_user', on_delete=models.CASCADE)
    rooms = models.ForeignKey(Room, related_name='booking_room', on_delete=models.CASCADE)

    def __str__(self):
        return self.rooms.title

    def get_absolute_url(self):
        return reverse('booking', kwargs={"room_id": self.rooms.pk})


class TypeService(models.Model):
    title = models.CharField(max_length=50, verbose_name="Вид сервиса", unique=True)
    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class ServiceHotel(models.Model):
    type = models.ForeignKey(TypeService, verbose_name="Сервис", on_delete=models.CASCADE)
    users = models.ForeignKey(User, related_name='service_user', on_delete=models.CASCADE)
    mark = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        verbose_name='Оценка')
