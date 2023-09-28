from django.contrib import admin

# Register your models here.

from .models import Payment
 
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']
    search_fields = ['user']
 

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user']

 

admin.site.register(Payment, PaymentAdmin)