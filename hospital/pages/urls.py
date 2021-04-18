from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('aboutUs/',views.AboutUs.as_view(),name='about'),
    path('contactUs/', views.ContactUsView, name='email_us'),
    path('success/', views.successView.as_view(), name='success'),
]
