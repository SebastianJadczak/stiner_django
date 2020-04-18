from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


def manage(request):
    return render(request,'management/manage.html')