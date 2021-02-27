from django.db import models

# Create your models here.
class current_price(models.Model):
    timestamp = models.BigIntegerField()
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    market = models.CharField(max_length=50)
    commodity = models.CharField(max_length=100)
    variety = models.CharField(max_length=50)
    arrival_date = models.DateField()
    min_price = models.FloatField()
    max_price = models.FloatField()
    model_price = models.FloatField()

class company(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.BigIntegerField()
    address = models.CharField(max_length=150)
    certificate = models.ImageField()
    logo = models.ImageField()

class commodity(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()

class contract(models.Model):
    company_id = models.ForeignKey('company',on_delete=models.CASCADE)
    commodity_id = models.ForeignKey('commodity',on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.CharField(max_length=30)
    deadline = models.CharField(max_length=20)
