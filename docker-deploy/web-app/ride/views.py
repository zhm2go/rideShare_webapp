from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewRideForm, NewRideSharer, NewRideDriver
from .models import Ride, RideSharer, RideDriver
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')
def new_ride(request):
    if request.method == 'POST':
        form = NewRideForm(request.POST)
        if form.is_valid():
            ride = form.save()
            ride.isComfirmed = False
            ride.totalNum = ride.numPassenger
            ride.caller = request.user
            ride.save()
            return redirect('ride_requested')
    else:
        form = NewRideForm()
    return render(request, 'new_ride.html', {'form':form})


@login_required(login_url='/login/')
def ride_made(request):
    #user = get_object_or_404(User, pk=pk)
    user = request.user
    ride_list = user.rideOwner.all().order_by('-arrivalTime')
    return render(request, 'finish_request.html', {'ride_list':ride_list})

@login_required(login_url='/login/')
def delete_ride(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    if not ride.isComfirmed:
        ride.delete()
    return redirect('ride_requested')

@login_required(login_url='/login/')
def modify_ride(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    other = ride.totalNum - ride.numPassenger
    if not ride.isComfirmed:
        if request.method == 'POST':
            form = NewRideForm(request.POST)
            if form.is_valid():
                new_ride = form.save()
                new_ride.totalNum = other + new_ride.numPassenger
                new_ride.caller = request.user
                new_ride.save()
                ride.delete()
                return redirect('ride_requested')
        else:
            form = NewRideForm(instance=ride)
        return render(request, 'modify_ride.html', {'form': form, 'pk':pk})
    return redirect('ride_requested')

@login_required(login_url='/login/')
def share_made(request):
    #user = get_object_or_404(User, pk=pk)
    user = request.user
    ride_list = user.sharer.all().order_by('-latest')
    return render(request, 'all_share_ride.html', {'ride_list': ride_list})

@login_required(login_url='/login/')
def new_share(request):
    if request.method == 'POST':
        form = NewRideSharer(request.POST)
        if form.is_valid():
            share = form.save()
            share.sharer = request.user
            share.save()
            #available_ride = Ride.objects.all().filter(isShare=True, isComfirmed=False, date__range=(share.earliest_date, share.latest_date))
            #available_ride = available_ride_date.filter(time__range=(share.earliest_time, share.latest_time))
            return redirect('share_requested')
    else:
        form = NewRideSharer()
    return render(request, 'new_share.html', {'form':form})

@login_required(login_url='/login/')
def delete_share(request, pk):
    share = get_object_or_404(RideSharer, pk=pk)
    if not share.isComfirmed:
        if share.ride:
            ride = share.ride
            ride.totalNum = ride.totalNum - share.numPassenger
            ride.save()
        share.delete()
    return redirect('share_requested')

@login_required(login_url='/login/')
def search_ride(request, pk):
    share = get_object_or_404(RideSharer, pk=pk)
    if not share.ride:
        available_rides = Ride.objects.all().filter(destination=share.destination, isShare=True, isComfirmed=False,
                                                   arrivalTime__range=(share.earliest, share.latest))
        return render(request, 'search_result.html', {'ride_list': available_rides, 'sharepk': pk})
    return redirect('share_requested')

@login_required(login_url='/login/')
def join_ride(request):
    if request.method == 'POST':
        rideId = int(request.POST['rideid'])
        shareId = int(request.POST['shareid'])
        ride = get_object_or_404(Ride, pk = rideId)
        share = get_object_or_404(RideSharer, pk = shareId)
        if not share.ride:
            ride.totalNum = ride.totalNum + share.numPassenger
            share.ride = ride
            share.save()
            ride.save()
            return redirect('share_requested')
    return redirect('share_requested')

@login_required(login_url='/login/')
def modify_share(request, pk):
    share = get_object_or_404(RideSharer, pk=pk)
    if request.method == 'POST':
        form = NewRideSharer(request.POST)
        if form.is_valid():
            new_share = form.save()
            if share.ride:
                ride = share.ride
                ride.totalNum = ride.totalNum - share.numPassenger
                ride.save()
            share.delete()
            new_share.sharer = request.user
            new_share.save()
            return redirect('share_requested')
    else:
        form = NewRideSharer(instance=share)
        return render(request, 'modify_share.html', {'form': form,'pk':pk})
    return redirect('share_requested')

@login_required(login_url='/login/')
def owner_details(request, pk):
    share = get_object_or_404(RideSharer, pk=pk)
    if not share.ride:
        return redirect('share_requested')
    ride = share.ride
    otherPa = ride.totalNum - share.numPassenger
    return render(request, 'ride_details.html', {'ride': ride, 'other':otherPa})

@login_required(login_url='/login/')
def share_details(request, pk):
    ride = get_object_or_404(Ride, pk = pk)
    shares = ride.toshare.all()
    return render(request, 'share_detail.html', {'shares':shares})

@login_required(login_url='/login/')
def new_driver(request):
    try:
        request.user.driver
        return redirect('home')
    except ObjectDoesNotExist:
        if request.method == 'POST':
            form = NewRideDriver(request.POST)
            if form.is_valid():
                driver = form.save()
                driver.duser = request.user
                request.user.isDriver = True
                driver.save()
                return redirect('driver_info')
        else:
            form = NewRideDriver()
        return render(request, 'new_driver.html', {'form':form})

@login_required(login_url='/login/')
def driver_info(request):
    try:
        request.user.driver
        return render(request, 'drive_info.html')
    except:
        return redirect('home')

@login_required(login_url='/login/')
def drive_modify(request):
    if not request.user.driver:
        return redirect('home')

    driver = request.user.driver
    if request.method == 'POST':
        form = NewRideDriver(request.POST)
        if form.is_valid():
            new_driver = form.save()
            driver.delete()
            new_driver.duser = request.user
            new_driver.save()
            return redirect('driver_info')
    else:
        form = NewRideDriver(instance=driver)
    return render(request, 'modify_driver.html', {'form': form})

@login_required(login_url='/login/')
def delete_driver(request):
    user = request.user
    if user.driver:
        user.driver.delete()
        return redirect('home')
    return redirect('home')

@login_required(login_url='/login/')
def driver_search(request):
    try:
        driver = request.user.driver
        ride_list = Ride.objects.all().filter(Q(special='') |Q(special=driver.special))
        ride_list = ride_list.filter(vehicleType=driver.vehicletype, totalNum__lte=driver.maxPassengers, isComfirmed=False)
        return render(request, 'driver_search_result.html', {'ride_list':ride_list})
    except:
        return redirect('home')

@login_required(login_url='/login/')
def check_confirmed_ride(request):
    try:
        var = request.user.driver
        return render(request, 'confirmed_ride.html')
    except:
        return redirect('home')

@login_required(login_url='/login/')
def confirm_ride(request, pk):
    ride = get_object_or_404(Ride, pk = pk)
    if ride.isComfirmed:
        return redirect('driver_search')
    ride.isComfirmed = True
    driver =request.user.driver
    ride.driver = driver
    ride.save()
    driver.save()
    subject = "Your ride has been confirmed!"
    msg = "Driver " + str(driver.duser.username) + " has confirmed your ride."
    sharers = ride.toshare.all()
    sharer_mails = [sharer.sharer.email for sharer in sharers]
    send_mail(
        subject,
        msg,
        settings.EMAIL_HOST_USER,
        [ride.caller.email] + sharer_mails,
        fail_silently=False,
    )
    return redirect('check_confiremed_ride')

@login_required(login_url='/login/')
def driver_complete(request):
    if request.method == 'POST':
        rideId = int(request.POST['rideid'])
        ride = get_object_or_404(Ride, pk=rideId)
        ride.delete()
    return redirect('check_confiremed_ride')

@login_required(login_url='/login/')
def view_driver_detail(request):
    if request.method == 'POST':
        rideId = int(request.POST['rideid'])
        ride = get_object_or_404(Ride, pk=rideId)
        driver = ride.driver
        return render(request, 'driver_details.html', {'driver':driver})
    return redirect('ride_requested')

def base(request):
    return render(request, 'base.html')