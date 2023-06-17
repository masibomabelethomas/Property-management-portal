from django.contrib import admin
from . models import Property_model, Tenant_model, Lease_model, MaintenanceRequest_model, Payment_model, Invoice_model
 
# Register your models here. 
# from .models import Product
# admin.site.register(Product){basic way to register}

# Customizations for the admin interface model registration.
class Property_modelAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'size', 'num_rooms', 'amenities', 'rental_price', 'status']
    list_filter = ['name', 'rental_price', 'size']
    search_fields = ['status', 'amenities']
 

class Tenant_modelAdmin(admin.ModelAdmin):
    # Customize the admin options for your model here
    list_display = ['lease']

class Lease_modelAdmin(admin.ModelAdmin):
    # Customize the admin options for your model here
    list_display = ['property']

class MaintenanceRequest_modelAdmin(admin.ModelAdmin):
    # Customize the admin options for your model here
    list_display = ['status']

class Payment_modelAdmin(admin.ModelAdmin):
    # Customize the admin options for your model here
    list_display = ['property']

class Invoice_modelAdmin(admin.ModelAdmin):
    # Customize the admin options for your model here
    list_display = ['property']


admin.site.register(Property_model, Property_modelAdmin)
admin.site.register(Tenant_model, Tenant_modelAdmin)
admin.site.register(Lease_model, Lease_modelAdmin)

admin.site.register(MaintenanceRequest_model, MaintenanceRequest_modelAdmin)
admin.site.register(Payment_model, Payment_modelAdmin)
admin.site.register(Invoice_model, Invoice_modelAdmin)
