from django.contrib import admin
from .models import Property_model
 
class Property_modelAdmin(admin.ModelAdmin):
    list_display = ['name','size', 'amenities', 'rental_price', 'status']
    list_filter = ['name', 'rental_price', 'size']
    search_fields = ['status', 'amenities']
 

class Tenant_modelAdmin(admin.ModelAdmin):
    list_display = ['name']

 

admin.site.register(Property_model, Property_modelAdmin)
 
 