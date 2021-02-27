from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
import requests
import pprint
# Create your views here.
def mandiprice(request):
    if request.method == 'POST':
        StateName=request.POST["StateName"]
        DistrictName=request.POST["DistrictName"]
        MarketName=request.POST["MarketName"]
        CommodityName=request.POST["CommodityName"]
        VarietyName=request.POST["VarietyName"]
        ArrivalDate=request.POST["ArrivalDate"]
        MinPrice=request.POST['MinPrice']
        MaxPrice=request.POST['MaxPrice']
        data_all= current_price.objects.all()
        data=[]
        state_set = set()
        district_set = set()
        market_set = set()
        commodity_set = set()
        variety_set = set()
        arrival_date_set = set()
        for i in data_all:
            state_set.add(i.state)
            district_set.add(i.district)
            market_set.add(i.market)
            commodity_set.add(i.commodity)
            variety_set.add(i.variety)
            date = str(i.arrival_date.day) + "-" + str(i.arrival_date.month) + "-" + str(i.arrival_date.year)
            arrival_date_set.add(date)
            if(StateName!="" and StateName!=i.state):
                continue
            if (DistrictName!="" and DistrictName != i.district):
                continue
            if (MarketName!="" and MarketName != i.market):
                continue
            if (CommodityName!="" and CommodityName != i.commodity):
                continue
            if (VarietyName!="" and VarietyName != i.variety):
                continue
            if (ArrivalDate!="" and ArrivalDate != date):
                continue
            if (MinPrice!="" and float(MinPrice) < i.min_price):
                continue
            if (MaxPrice!="" and float(MaxPrice) > i.max_price):
                continue
            data.append(i)



    else:
        data=current_price.objects.all()
        state_set=set()
        district_set=set()
        market_set=set()
        commodity_set=set()
        variety_set=set()
        arrival_date_set=set()
        for i in data:
            state_set.add(i.state)
            district_set.add(i.district)
            market_set.add(i.market)
            commodity_set.add(i.commodity)
            variety_set.add(i.variety)
            date=str(i.arrival_date.day)+"-"+str(i.arrival_date.month)+"-"+str(i.arrival_date.year)
            arrival_date_set.add(date)
    return render(request,'mandiprice.html',{'data':data,'state_set':sorted(state_set),'district_set':sorted(district_set),
                                             'market_set':sorted(market_set),'commodity_set':sorted(commodity_set),
                                             'variety_set':sorted(variety_set),
                                             'arrival_date_set':sorted(arrival_date_set)})

def login(request):
    if request.method == 'POST':
        company_email = request.POST['companyemail']
        password = request.POST['password']
        flag=0
        companies_all=company.objects.all()
        for company_p in companies_all:
            if company_p.email==company_email and company_p.password==password:
                flag=1
                return redirect('home.html')
        if flag==0:
            return redirect('login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        company_name = request.POST['companyName']
        email_id = request.POST['Email']
        if company.objects.filter(email=email_id).exists():
            messages.info(request, "Email ID Already Exists!")
            return render(request,'signup.html')
        contact = request.POST['cNumber']
        address1 = request.POST['add1']
        address2 = request.POST['add2']
        address3 = request.POST['add3']
        password = request.POST['pass']
        logo=request.POST['logo']
        certi=request.POST['certi']
        obj=company()
        obj.name=company_name
        obj.email=email_id
        obj.contact=contact
        obj.password=password
        obj.address=str(address1)+"&&"+str(address2)+"&&"+str(address3)
        obj.logo=logo
        obj.certificate=certi
        obj.save()
        return render(request,'home.html')
    else:
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