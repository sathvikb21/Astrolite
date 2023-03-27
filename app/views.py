from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import UserDetail
from django.contrib.auth.models import User


def homepage(request):
    return render(request, 'index.html')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/dashboard')
        return render(request, 'login.html')


def signuppage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        firstname, lastname = name.split(' ', 1)
        print(firstname)
        print(lastname)

        newuser = User.objects.create_user(
            username=username, first_name=firstname, last_name=lastname, password=password)
        newuser.save()

        user = authenticate(request, username=username, password=password)
        UserDetail.objects.create(
            username=username,
            total_trips=0,
            upcoming_trips=0,
            total_distance=0,
            total_cost=0,
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request, 'signup.html')


def logoutpage(request):
    logout(request)
    return redirect('home')