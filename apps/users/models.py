from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')

    def __str__(self):
        return f"{self.user.username}'s profile"


@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)