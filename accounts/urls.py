from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('signup/doctor/', views.DoctorCreateView.as_view(), name='doctor_signup'),
    path('signup/doctor/', views.doctor_sign_up_view, name='doctor_signup'),
    #path('signup/patient/', views.PatientSignUpView.as_view(), name='patient_signup'),
    path('signup/patient/', views.patient_sign_up_view, name='patient_signup'),
    path('reset_password',views.ResetPassword.as_view(),name='reset_password_form'),
]