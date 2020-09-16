from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField
from ckeditor.fields import RichTextField


class CarType(models.Model):
    # @TODO: Rename or something
    model = models.CharField(max_length=255) # eg. merceddes
    sub_category = models.CharField(max_length=255) # eg. benz v1

    class Meta:
        unique_together = ('model', 'sub_category',)


class Cars(models.Model):
    owner = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
    car_type = models.ForeignKey('CarType', related_name='cars', on_delete=models.PROTECT)
    picture = VersatileImageField()
    about = RichTextField(blank=True)


class Event(models.Model):
    car = models.ForeignKey('Cars', related_name='event', on_delete=models.CASCADE)
    date = models.DateTimeField()
    about = RichTextField(blank=True)
    repeat_time = models.DateTimeField() #?
