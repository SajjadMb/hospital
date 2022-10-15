from django.db import models
from accounts.models import Patient,Doctor

# Create your models here.
class Reservation(models.Model):
    patient = models.OneToOneField(Patient,on_delete=models.CASCADE)

    doctor = models.OneToOneField(Doctor,on_delete=models.CASCADE)

    reservation_date = models.DateField(blank=True, null=True)
    reservation_turn = models.BigIntegerField()