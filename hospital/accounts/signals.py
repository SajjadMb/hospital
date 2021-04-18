from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print("signal worked")
    instance.profile.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Doctor)
def save_profile(sender, instance, **kwargs):
    print("signal worked")
    instance.user.save()


@receiver(post_save, sender=Doctor)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)


@receiver(post_save, sender=Patient)
def save_profile(sender, instance, **kwargs):
    print("signal worked")
    instance.user.save()


@receiver(post_save, sender=Patient)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("signal worked")
        User.objects.create(user=instance)
