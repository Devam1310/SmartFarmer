from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
import requests
import pprint
# Create your views here.
def mandiprice(request):
    data=current_price.objects.all()
    return render(request,'mandiprice.html',{'data':data})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')

def contracts(request):
    return render(request,'contracts.html')

def addcontract(request):
    return render(request,'addcontract.html')

def pricedata(request):
    current_price.objects.all().delete()
    string1="Data Deleted"
    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    param = {'api-key': '579b464db66ec23bdd0000019336711b91634c2c6890289890100ae0', 'format': 'json', 'limit': 5000}
    data = requests.get(url, param).json()
    length = len(data['records'])
    count=0
    commodity_list=commodity.objects.all()
    commodities=set()
    for i in commodity_list:
        commodities.add(i.name)
    print(commodities)
    commodity.objects.all().delete()
    for i in range(length):
        print(count)
        count=count+1
        cur=data['records'][i]
        commodities.add(cur['commodity'])
        date=cur['arrival_date']
        date=date[6:10] + "-" + date[3:5] + "-" + date[0:2]
        current_price.objects.create(timestamp=cur['timestamp'],state=cur['state'],district=cur['district'],
                                     market=cur['market'],commodity=cur['commodity'],variety=cur['variety'],
                                     arrival_date=date,min_price=cur['min_price'],max_price=cur['max_price'],
                                     model_price=cur['modal_price'])
    string2="Data Successfully Updated! No of rows : {}".format(count)
    for element in commodities:
        commodity.objects.create(name=element)
    string3="{} Commodities Added".format(len(commodities))
    string="<h1>{}</h1>".format(string1+"\n"+string2+"\n"+string3)
    return HttpResponse(string)