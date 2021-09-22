from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

# Create your views here.
from .forms import CreateUserForm

from django.contrib import messages



def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('view_fmea')
    context={}
    return render(request,"login.html",context)

def register(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created Sucessfully")
            return redirect('login')
    context={'form':form}
    return render(request,'register.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')