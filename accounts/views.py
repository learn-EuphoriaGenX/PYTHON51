from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def Login(request):

    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['user_password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or Password')

    return render(request, 'login.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        email = request.POST['user_email']
        password = request.POST['user_password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else :
            newUser = User.objects.create_user(username=username, email=email, password=password)
            newUser.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
        
    return render(request, 'register.html')

def Logout(request):
    logout(request)
    return redirect('login')