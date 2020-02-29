from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


# class RiderOwner(models.Model):
#
#     destination = models.CharField(max_length=100)
#     arrivalTime = models.DateTimeField()
#     numPassenger = models.IntegerField()
#     isShare = models.BooleanField()
#     isComfirmed = models.BooleanField()
#     caller = models.ForeignKey(User, related_name="ride", on_delete=models.CASCADE)
#
#
# class RiderDriver(models.Model):
#
#     plate = models.CharField(max_length=10)
#     vehicleType = models.CharField(max_length=20)
#     special = models.TextField(max_length=2000)
#     user = models.ForeignKey(User, related_name="driver", on_delete=models.CASCADE)
#     ride = models.ForeignKey(RiderOwner, related_name="driver", on_delete=models.CASCADE)

class MyTest(models.Model):
    name = models.CharField(max_length=50)
    num = models.IntegerField()


class RideDriver(models.Model):
    VEHICLE_TYPE_CHOICE = (
        ('micro', 'micro'),
        ('SUV', 'SUV'),
        ('VAN', 'VAN'),
        ('sedan', 'sedan'),
        ('CUV', 'CUV'),
    )
    vehicletype = models.CharField(max_length=6, default='sedan', choices=VEHICLE_TYPE_CHOICE)
    plate = models.CharField(max_length=10)
    maxPassengers = models.IntegerField()
    special = models.CharField(max_length=1000, null=True, blank=True)
    duser = models.OneToOneField(User, related_name='driver', on_delete=models.CASCADE, null = True)


class Ride(models.Model):
    VEHICLE_TYPE_CHOICE = (
        ('micro','micro'),
        ('SUV','SUV'),
        ('VAN','VAN'),
        ('sedan','sedan'),
        ('CUV','CUV'),
    )
    destination = models.CharField(max_length=100)
    arrivalTime = models.DateTimeField(null=True)
    numPassenger = models.IntegerField()
    totalNum = models.IntegerField(null=True)
    isShare = models.BooleanField(default=False)
    isComfirmed = models.BooleanField(default=False)
    vehicleType = models.CharField(max_length=16, default='sedan', choices=VEHICLE_TYPE_CHOICE)
    special = models.TextField(max_length=1000, null=True, default=None)
    caller = models.ForeignKey(User, related_name="rideOwner", on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(RideDriver, related_name='ride', on_delete=models.CASCADE, null=True)


class RideSharer(models.Model):
    destination = models.CharField(max_length=100)
    earliest = models.DateTimeField(null=True)
    latest = models.DateTimeField(null=True)
    numPassenger = models.IntegerField()
    isComfirmed = models.BooleanField(default=False)
    #owner = models.ForeignKey(User, related_name='shareOwner', on_delete=models.CASCADE, null=True)
    sharer = models.ForeignKey(User, related_name='sharer', on_delete=models.CASCADE, null=True)
    ride = models.ForeignKey(Ride, related_name='toshare', on_delete=models.CASCADE, null=True)