# accounts.models.py
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)  # a superuser
    staff = models.BooleanField(default=True)
    doctor_user = models.BooleanField(default=False)
    patient_user = models.BooleanField(default=False)


    # "Password field"'s built in.

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',)
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        blank=True, null=True
    )
    phone_number = PhoneNumberField(blank=True, null=True)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ensurance_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.email


class Doctor(models.Model):
    SPECIFICATIONS = (
            ('neurologist','neurologist'),
            ('dentist','dentist'),
            ('urologist','urologist')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specifications = models.CharField(
        max_length=50,
        choices=SPECIFICATIONS,
        blank=True, null=True
    )
    personal_num = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.email



