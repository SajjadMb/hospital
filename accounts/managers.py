from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('User must have a password')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.staff = True
        user.patient_user = False
        user.doctor_user = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = True
        user.save(using=self._db)
        return user

    def create_doctor(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.doctor_user = True
        user.save(using=self._db)
        return user

    def create_patient(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.patient_user = True
        user.save(using=self._db)
        return user
