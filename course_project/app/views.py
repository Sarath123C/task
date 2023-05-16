from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == "POST":
    #     form=UserCreationForm(request.POST)
    # if form.is_valid():
    #     form.save()
        username = request.POST['username']
        password1 = request.POST['confirm_password']
        password = request.POST['password']
        if password == password1:

            myuser = User.objects.create_user(username, password1, password)
            myuser.save()

            return redirect('login')
    return render(request,'register.html',{'form':form})
def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('form')
        else:
            return HttpResponse("not user")
    return render(request,'login.html')
def form(request):
    return render(request,'form.html')
def forum(request):
    return render(request,'forum.html')
def fill(request):
    return HttpResponse("Successfully Created")