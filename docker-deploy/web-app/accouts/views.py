from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.isDriver = False
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/login/')
def my_account(request):
    return render(request, 'my_account.html')

@login_required(login_url='/login/')
def edit_email(request):
    if request.method == "POST":
        p = request.POST
        new_email = request.POST['email']
        request.user.email = new_email
        request.user.save()
        return redirect('my_account')
    return render(request, 'change_email.html')