from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **_):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
