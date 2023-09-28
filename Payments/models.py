from django.db import models

# Create your models here.
from django.db import models
from coreApp.models import Property_model
from accounts.models import UserAccount  # If you're using the built-in User model

class Payment(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='payments')
    property = models.ForeignKey(Property_model, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    date_paid = models.DateField(auto_now_add=True)
    # date_paid = models.DateField()

def __str__(self):
        return f'Payment for {self.property} by {self.property}'

def __str__(self):
    return self.name   

