from django.urls import path
from . import views

urlpatterns=[
    path('mandiprice',views.mandiprice,name="mandiprice"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name='signup'),
    path('contracts', views.contracts, name="contracts"),
    path('addcontract', views.addcontract, name="addcontract")
]