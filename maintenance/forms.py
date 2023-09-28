from django import forms
# from maintenance import models
from .models import MaintenanceRequest

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['property','user', 'description', 
                  'priority','title',
                   'attachments']
