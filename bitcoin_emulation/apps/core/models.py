from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    private_key = models.CharField(max_length=100)
    public_key = models.CharField(max_length=100)
    
    def __unicode__ (self):
      return self.user.email

    @receiver(post_save, sender=User)
    def create_user_userinfo(sender, instance, created, **kwargs):
        if created:
            UserInfo.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_userinfo(sender, instance, **kwargs):
        instance.userinfo.save()

class Product(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    in_shop = models.BooleanField(default=True)
