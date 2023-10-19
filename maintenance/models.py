from django.db import models
from django.contrib.auth.models import User
from coreApp.models import Property_model
# from django.contrib.auth.models import User
# from accounts.models import UserAccount  
name = 'maintenance'
# Create your models here.

class MaintenanceRequest(models.Model):
    # Fields for the maintenance request
    property = models.ForeignKey(Property_model, on_delete=models.CASCADE, related_name='maintenance_requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maintenance_requests')
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    attachments = models.FileField(blank=True, null=True)
     
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')

    def __str__(self):
        return self.property
