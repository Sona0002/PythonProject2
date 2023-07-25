from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Photos

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Photos.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})

# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("hello world")

