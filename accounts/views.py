from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def signup(request):
    if request.method == 'POST':
        #the user wants to signup
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',{'error':'Username already Exist..!!'})

            except :
                user = User.objects.create_user(request.POST['username'],  password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')



            #will do this code later
        else :
            return render(request, 'accounts/signup.html',{'error':'password dosen\'t matched..!!'})

    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'Username or Password is Incorrect..!!'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
