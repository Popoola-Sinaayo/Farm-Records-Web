from django.db import models

# Create your models here.


class Farmer(models.Model):
    name = models.CharField(max_length=20)
    farm_name = models.CharField(max_length=30)


class Tractor(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        Farmer, related_name='real_owner', on_delete=models.CASCADE)
    harrow = models.BooleanField(default=False)
    cultivator = models.BooleanField(default=False)
    rotavator = models.BooleanField(default=False)
    plough = models.BooleanField(default=False)
    paddy_trasher = models.BooleanField(default=False)
    dumping_trailer = models.BooleanField(default=False)
    four_wheel_trailer = models.BooleanField(default=False)
