from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    user:User=instance
    if created:
        Profile.objects.create(
            user=user,
        )