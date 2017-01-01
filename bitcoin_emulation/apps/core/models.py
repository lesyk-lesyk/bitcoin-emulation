from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    pass_hash = models.CharField(max_length=100)
    email_hash = models.CharField(max_length=100)
    checksum = models.CharField(max_length=100)
    
    def __unicode__ (self):
      return self.text

    @receiver(post_save, sender=User)
    def create_user_userinfo(sender, instance, created, **kwargs):
        if created:
            UserInfo.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_userinfo(sender, instance, **kwargs):
        instance.userinfo.save()