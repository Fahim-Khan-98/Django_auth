from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def home(request):
    return render(request,'home.html')


def registerRequest(request):
    if request.user.is_authenticated:
        return HttpResponse("You are autenticated..")
    else:
        form = NewUserForm()
        if request.method == 'post' or request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)

                messages.success(request,'Registration successful.')
                return redirect("account:home")

            messages.error(request,'Unsuccessful Registration. Invalid Information!!')

        return render (request,'register.html',{'form':form})


def loginRequest(request):
    if request.method == 'post' or request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}.")
                return redirect("account:home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,'login.html',{"form": form})

def logoutRequest(request):
    logout(request)
    messages.info(request,'You have successfully logged out')
    return redirect("account:home")