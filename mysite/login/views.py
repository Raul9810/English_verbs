from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request,'login.html',{'Hola':'hola'})