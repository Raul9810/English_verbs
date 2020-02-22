from django.shortcuts import render
from django.http import HttpResponse
from .models import Word

def index(request):
    consulta = Word.objects.all()
    context = {
        'context':consulta
    }
    return render(request,'../templates/indez.html',context)