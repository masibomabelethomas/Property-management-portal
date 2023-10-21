from django.db import models
# from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
name = 'coreApp'
class Property_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    start_date= models.DateField(auto_now_add=True)
    end_date= models.DateField(auto_now_add=True)
    duration = models.DurationField()
    date_paid = models.DateField(blank=True, null=True)
    AMENITIES_CHOICES = [
        ('Balcony', 'Balcony'),
        ('Gym', 'Gym'),
        ('Swimming Pool', 'Swimming Pool')]
    STATUS_CHOICES=[
        ('Available','Available'),
        ('Occupied', 'Occupied') ]
    TYPE_OF_HOUSE =[('Single_room','Singleroom'),('Bedsitter','Bedsitter'),
                    ('One bedroom','One bedroom'),('Two bedroom','Two bedroom'),
                    ('Three bedroom','Three bedroom'),('Four bedroom','Four bedroom'),
                    ('Studio','Studio'),('commercial shops','commercial shops')]
    HOUSE_SIZE = [('STANDARD','STANDARD'), ('Spacious','Spacious')]
    amenities = models.TextField(choices=AMENITIES_CHOICES)
    status = models.TextField(choices=STATUS_CHOICES)
    house_type = models.PositiveIntegerField(choices=TYPE_OF_HOUSE)
    size = models.PositiveIntegerField(choices=HOUSE_SIZE)
    
    def __str__(self):
        return f"{self.property} - {self.user}"

    def save(self, *args, **kwargs):
        self.duration = self.end_date - self.start_date
        super().save(*args, **kwargs)
         
        
        
    # def duration(self):
    #     if self.start_date and self.end_date:
    #         return self.end_date - self.start_date
    #     else:
    #         return None





