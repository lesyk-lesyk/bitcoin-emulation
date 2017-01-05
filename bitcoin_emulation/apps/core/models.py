from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# class UserInfo(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     some_field = models.CharField(max_length=100)
    
#     def __unicode__ (self):
#       return self.user.email

#     @receiver(post_save, sender=User)
#     def create_user_userinfo(sender, instance, created, **kwargs):
#         if created:
#             UserInfo.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_userinfo(sender, instance, **kwargs):
#         instance.userinfo.save()

class Product(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    in_shop = models.BooleanField(default=True)
    public_x = models.CharField(max_length=500)
    public_y = models.CharField(max_length=500)    

class KeyPair(models.Model):
    owner = models.ForeignKey(User)
    private = models.CharField(max_length=500)
    public_x = models.CharField(max_length=500)
    public_y = models.CharField(max_length=500)
    status = models.CharField(max_length=50, default="active")
    amount = models.IntegerField(default=0)

class Block(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    prev_hash = models.CharField(max_length=500, default='')
    nonce = models.IntegerField(default=0)
    transactions_hash = models.CharField(max_length=500, default='')

class Transaction(models.Model):
    block = models.ForeignKey(Block, null=True)
    status = models.CharField(max_length=50, default="pending")

class Input(models.Model):
    transaction = models.ForeignKey(Transaction)
    address_x = models.CharField(max_length=500)
    address_y = models.CharField(max_length=500)
    signature_r = models.CharField(max_length=500)
    signature_s = models.CharField(max_length=500)
    

class Output(models.Model):
    transaction = models.ForeignKey(Transaction)
    address_x = models.CharField(max_length=500)
    address_y = models.CharField(max_length=500)
    amount = models.IntegerField(default=0)

# class Address(models.Model):
#     owner = models.ForeignKey(User)
#     x = models.IntegerField(default=0)
#     y = models.IntegerField(default=0)