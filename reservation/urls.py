# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', room_list, name='room-list'),
    path('booking/<int:id_room>/', booking, name='booking')
]