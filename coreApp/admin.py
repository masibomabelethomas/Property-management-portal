from django.contrib import admin
from .models import Property_model, Booking
 
class Property_modelAdmin(admin.ModelAdmin):
    list_display = ['property_name','size', 'amenities', 'rental_price', 'status']
    list_filter = ['property_name', 'rental_price', 'size']
    search_fields = ['status', 'amenities']
 

class Tenant_modelAdmin(admin.ModelAdmin):
    list_display = ['property_name']

 
class BookingAdmin(admin.ModelAdmin):
 list_display = ['property','check_in_date','check_out_date','number_of_guests','created_at']
 list_filter = ['property','check_in_date','check_out_date',]
 search_fields =['property']

 admin.site.register(Property_model, Property_modelAdmin)
admin.site.register(Booking, BookingAdmin)
 


