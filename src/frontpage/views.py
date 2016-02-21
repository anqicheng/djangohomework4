from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    all_object = blog.objects.all()
    zero_object = all_object[0]
    first_object=all_object[1]
    zero_object_title=zero_object.title

    template="home.html"
    context={
    "all_object": all_object,
    "zero_object": zero_object,
    "first_object": first_object,
    "zero_object_title": zero_object_title,
    }
    return render(request, template,context)