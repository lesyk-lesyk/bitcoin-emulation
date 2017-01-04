from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# from models import UserInfo
from models import Product
from models import KeyPair, Block, Transaction, Input, Output

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
admin.site.register(Input)
admin.site.register(Output)


class TransactionInline(admin.StackedInline):
    model = Transaction
    can_delete = False
    verbose_name_plural = 'Transactions'

class BlockAdmin(admin.ModelAdmin):
   inlines = (TransactionInline,)
   readonly_fields = ('timestamp',)

admin.site.register(Block, BlockAdmin)


class InputInline(admin.StackedInline):
    model = Input
    can_delete = False
    verbose_name_plural = 'Inputs'

class OutputInline(admin.StackedInline):
    model = Output
    can_delete = False
    verbose_name_plural = 'Outputs'    

class TransactionkAdmin(admin.ModelAdmin):
   inlines = (InputInline, OutputInline)

admin.site.register(Transaction, TransactionkAdmin)
