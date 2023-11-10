from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import People

# Create your views here.

# def travels(request):
#     return HttpResponse("hello world")


def demo(request):
    obj1=Place.objects.all()
    obj2 = People.objects.all()

    return render(request,"index.html",{'result1':obj1,'result2':obj2})

