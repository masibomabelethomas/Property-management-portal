from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()
# from django.contrib.auth.models import User
# from django.db import models
from coreApp.models import Property_model

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    property = models.ForeignKey(Property_model, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    date_paid = models.DateField(auto_now_add=True)
def __str__(self):
        return f'Payment for {self.property} by {self.property}'

def __str__(self):
    return self.name   

