from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class TypeRoom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'room type: {self.name}'

class Room(models.Model):
    number = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    place = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='rooms_image')
    type_room = models.ForeignKey(TypeRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f'number - {self.number}, price - {self.price}, place - {self.place}'



    class Meta:
        ordering = ['price']  # Сортування за ціною
        verbose_name = "room"  # Назва в однині в адмінці
        verbose_name_plural = "Rooms" #Назва в множині



class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    date_creation = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    people_quantity =  models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'start: {self.date_start}, end: {self.date_end}, date create: {self.date_creation}'




    class Meta:
        ordering = ['date_creation', 'date_start', 'date_end']  # Сортування за ціною
        verbose_name = "Reservation"  # Назва в однині в адмінці
        verbose_name_plural = "Reservations" #Назва в множині



