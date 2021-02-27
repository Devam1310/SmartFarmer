from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def mandiprice(request):
    return render(request,'mandiprice.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')

def contracts(request):
    return render(request,'contracts.html')

def addcontract(request):
    return render(request,'addcontract.html')