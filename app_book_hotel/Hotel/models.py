from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    title = models.CharField(max_length=124, verbose_name='Название номера')
    desc = models.TextField(verbose_name='Описание номера', max_length=500, blank=True)
    size = models.PositiveSmallIntegerField(verbose_name='Площадь номера')
    smoke = models.BooleanField(default=True, verbose_name='Не курят')
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


class Facilities(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название удобства", unique=True)
    photo = models.ImageField(verbose_name='Иконка', upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title



# Create your models here.
