from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Indexview, name='registerpage'),
    path('insert/',views.insert,name='insert'),
    path('login/',views.Loginview, name='loginpage'),
]