from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField


class CarType(models.Model):
    # @TODO: Rename or something
    model = models.CharField(max_length=255) # eg. merceddes
    sub_category = models.CharField(max_length=255)# eg. benz v1

    class Meta:
        unique_together = ('model', 'sub_category',)


class Cars(models.Model):
    owner = models.ForeignKey('User', related_name='cars', on_delete=models.CASCADE)
    car_type = models.ForeignKey('CarType', related_name='cars', on_delete=models.PROTECT)
    # make = models.
    # model = models.
    # owner = models.Foreignkey(User, on_delete=models.CASCADE)
    # picture = models.VersatileImageField()
    # about = models.RichText()


class Event(models.Model):
    pass
    # car = models.Foreignkey(Cars, on_delete=models.CASCADE)
    # date = models.DateTimeField(default=timezone.now)
    # about = models.RichText()
    # repeat_time = models.Datetime()
