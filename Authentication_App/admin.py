# from django.contrib import admin
# from .models import CustomUser
# from django import forms

# # from Authentication_App.models import CustomAccountManager

# # # this code is to customize the disaply fields and the entire admin area.
# class UserAdminConfig(CustomUser):
#     model = CustomUser
#     search_fields =('email', 'user_name', 'first_name',)
#     list_filter = ('email','user_name','filter_name', 'is_active','is_staff')
#     ordering = ('-start_date',)
#     list_display = ('email','user_name', 'first_name',' is_active', 'is_staff')

#     fieldsets = (
#         (None, {'fields': ('email','user_name','first_name',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#         ('Personal', {'fields': ('about',)}),
#     )
#     formfield_overrides = {
#         CustomUser.about: {'widget': forms.Textarea(attrs={'rows':10, 'cols':40})},
#     }

#     add_fieldsets = (
#     (None, {
#         'classes':('wide',),
#         'fields':('email', 'user_name','first_name','password1','password2','is_active', 'is_staff'),
#     })
# )
    
# admin.site.register(CustomUser, UserAdminConfig)
# # admin.site.register(CustomUser)