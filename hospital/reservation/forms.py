from django import forms
from accounts.models import Doctor
from .models import Reservation

class SearchDoctorForm(forms.ModelForm):

     class Meta:
         model = Doctor
         fields = ('specifications',)


class ReservationForm(forms.ModelForm):

     class Meta:
         model = Reservation
         fields = '__all__'
         exclude = ('reservation_turn',)