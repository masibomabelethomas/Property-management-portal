from django.contrib import admin
from . models import Property_model, Tenant_model
 
class Property_modelAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'size', 'num_rooms', 'amenities', 'rental_price', 'status']
    list_filter = ['name', 'rental_price', 'size']
    search_fields = ['status', 'amenities']
 

class Tenant_modelAdmin(admin.ModelAdmin):
    list_display = ['name']

 

admin.site.register(Property_model, Property_modelAdmin)
admin.site.register(Tenant_model, Tenant_modelAdmin)
 