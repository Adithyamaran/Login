from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.login,name="login"),
    path('log',views.log,name="log"),
    path('getclass',views.classinfo,name="classinfo")
]