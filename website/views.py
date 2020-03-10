from django.shortcuts import render
from django.http import request


def home(request):
    return render(request, 'website/index.html')
# Create your views here.
