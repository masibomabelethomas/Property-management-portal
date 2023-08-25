from django.contrib import admin
from . models import Property_model, Tenant_model, Lease_model
# from Authentication_App.models import CustomUser

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
 

admin.site.register(Property_model, Property_modelAdmin)
admin.site.register(Tenant_model, Tenant_modelAdmin)
admin.site.register(Lease_model, Lease_modelAdmin)


# admin.site.register(CustomUser)