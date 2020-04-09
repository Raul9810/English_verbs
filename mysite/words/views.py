from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Word,Noun, Adjective, Adverb, Expresion, Phrasal, Verb

dic = {1:Word,2:Noun,3:Adjective,4:Adverb,5:Expresion,6:Phrasal,7:Verb}

def index(request):
    consulta = Word.objects.all()
    context = {
        'context':consulta
    }
    return render(request,'words.html',context)

def getWord(request, id=-1, typeW=1):

    consulta = Word.objects.all()
    if id != -1:
        consulta = get_object_or_404(dic[typeW], pk=id)
    
    context = {
        'context':consulta
    }
    return render(request,'words.html',context)
        