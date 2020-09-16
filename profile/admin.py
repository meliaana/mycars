from django.contrib import admin
from .models import CarType, Cars, Event

admin.site.register(Cars)
admin.site.register(CarType)
admin.site.register(Event)