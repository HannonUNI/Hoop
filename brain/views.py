from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from . import models


# from .forms import CustomUserCreationForm


# Create your views here.
def index(request):
    return render(request, 'brain/home.html')


def accountManage(request):
    # if request.method == 'POST':
    #     register(request)
    return render(request, 'brain/accounts.html')


def register(request):
    if request.method == "POST":
        if request.POST.get('submit') == "register":
            form = UserCreationForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                print(form.errors)
                return redirect('bad register')
        else:
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                print('success')
                return redirect('index')
            else:
                print('fail')
    else:
        print("GET")


def contests(request, id=None):
    if not id:
        return render(request, 'brain/contests.html')

    contest = models.Contest.objects.get(id=id)
    context = {
        'contest': contest
    }
    return render(request, 'brain/contests.html', context)
    