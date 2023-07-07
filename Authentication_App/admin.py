from django.contrib import admin
from .models import CustomUser
# from myapp.models import CustomUser
from Authentication_App.models import CustomAccountManager

# Register your models here.

admin.site.register(CustomUser)
# admin.site.register(CustomAccountManager)