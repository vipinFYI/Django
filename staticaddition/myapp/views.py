from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm




# Create your views here.


def home_view(request):
    return render(request,'home.html')


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password = password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})
