from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# from models import UserInfo
from models import Product
from models import KeyPair

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class UserInfoInline(admin.StackedInline):
#     model = UserInfo
#     can_delete = False
#     verbose_name_plural = 'userInfo'

class KeyPairInline(admin.StackedInline):
    model = KeyPair
    can_delete = False
    verbose_name_plural = 'KeyPairs'

class PruductInline(admin.StackedInline):
    model = Product
    can_delete = False
    verbose_name_plural = 'Products'    

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (KeyPairInline, PruductInline)
  
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(KeyPair)
