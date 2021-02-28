from django.urls import path
from . import views

urlpatterns=[
    path('', views.plantai, name="plantai"),
    path('predict', views.predict, name='predict'),
    # path('signUP',views.signUP,name="signUP"),
    # path('userHome',views.signIN,name="signIN"),
    # path('logOut',views.logOut,name='logOut'),
    # path('searchbar', views.searchbar, name="search")
]
