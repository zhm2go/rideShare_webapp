from django import forms
from .models import Ride, RideSharer, RideDriver
from bootstrap3_datetime.widgets import DateTimePicker


class NewRideForm(forms.ModelForm):
    VEHICLE_TYPE_CHOICE = (
        ('micro', 'micro'),
        ('SUV', 'SUV'),
        ('VAN', 'VAN'),
        ('sedan', 'sedan'),
        ('CUV', 'CUV'),
    )
    special = forms.CharField(widget=forms.Textarea(), max_length=1000, required=False,initial=None)
    arrivalTime = forms.DateTimeField(label='Arrival Time')
    numPassenger = forms.IntegerField(label='Number of Passengers')
    isShare = forms.BooleanField(label='Is your ride sharable?', required=False, initial=False)
    vehicleType = forms.ChoiceField(label='Choose your vehicle type?', choices=VEHICLE_TYPE_CHOICE)
    class Meta:
        model = Ride
        fields = ['destination', 'arrivalTime', 'numPassenger', 'isShare', 'vehicleType','special']


class NewRideSharer(forms.ModelForm):
    earliest = forms.DateTimeField(label='Earliest Time')
    latest = forms.DateTimeField(label='Latest Time')
    class Meta:
        model = RideSharer
        fields = ['destination', 'earliest', 'latest','numPassenger']


class NewRideDriver(forms.ModelForm):
    VEHICLE_TYPE_CHOICE = (
        ('micro', 'micro'),
        ('SUV', 'SUV'),
        ('VAN', 'VAN'),
        ('sedan', 'sedan'),
        ('CUV', 'CUV'),
    )
    special = forms.CharField(widget=forms.Textarea(), max_length=1000, required=False)
    plate = forms.CharField(label='Plate number')
    maxPassengers = forms.IntegerField(label='Max number of passengers')
    vehicletype = forms.ChoiceField(label='Choose your vehicle type?', choices=VEHICLE_TYPE_CHOICE)
    class Meta:
        model = RideDriver
        fields = ['vehicletype', 'plate', 'maxPassengers', 'special']