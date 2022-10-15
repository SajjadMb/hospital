from django.urls import path

from . import views


urlpatterns = [
    path('search_doctor/', views.searchDoctor.as_view(), name='searchDoctor'),
    path('appointment/(?U<str:username>/)',views.appointment.as_view(),name='appointment')
]