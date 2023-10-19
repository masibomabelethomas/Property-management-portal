from django.contrib import admin

from .models import MaintenanceRequest
 
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ['property','user', 'description', 
                  'priority','title', 'attachments']
    list_filter = ['property','user', 'description']
    search_fields = ['priority','title']
 
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ['property']

 
admin.site.register(MaintenanceRequest, MaintenanceRequestAdmin)
 


