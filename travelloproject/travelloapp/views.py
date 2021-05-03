from django.shortcuts import render
from .models import place,blog
# Create your views here.
def fun(request):
    obj=place.objects.all()
    ob= blog.objects.all()
    return render(request,"index.html",{'results':obj,'a':ob})