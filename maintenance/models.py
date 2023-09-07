from django.db import models
from .models import Property_model
from django.contrib.auth.models import User 

name = 'maintenance'
# Create your models here.

class MaintenanceRequest(models.Model):
    # Fields for the maintenance request
    property = models.ForeignKey(Property_model, on_delete=models.CASCADE, related_name='maintenance_requests')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maintenance_requests')
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Status and Priority fields
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    
    # Assigned To field (linked to User)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Attachments field for file uploads
    attachments = models.FileField(upload_to='maintenance_attachments/', blank=True, null=True)
    
    # Feedback field
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
