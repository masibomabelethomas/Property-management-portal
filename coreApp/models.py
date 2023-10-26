from django.db import models
# from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from datetime import datetime

name = 'coreApp'
class Property_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property')
    property_name = models.CharField(max_length=255)
    location = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)

    start_date = models.start_date = datetime.now()
    end_date = models.end_date = datetime.now()

    duration = models.DurationField()
    date_paid = models.DateField(blank=True, null=True)

    AMENITIES_CHOICES = [
        ('Balcony','Balcony'),
        ('Gym','Gym'),
        ('SwimmingPool','SwimmingPool')]
    
    STATUS_CHOICES=[
        ('Available','Available'),
        ('Occupied', 'Occupied') ]
    
    HOUSE_SIZE = [('STANDARD','STANDARD'), 
                  ('Spacious','Spacious')]
    
    TYPE_OF_HOUSE =[('Singleroom','Singleroom'),
                    ('Bedsitter','Bedsitter'),
                    ('Onebedroom','Onebedroom'),
                    ('Twobedroom','Twobedroom'),
                    ('Threebedroom','Threebedroom'),
                    ('Fourbedroom','Fourbedroom'),
                    ('Studio','Studio'),
                    ('Commercialshops','Commercialshops')]
    
    amenities = models.TextField(choices=AMENITIES_CHOICES)
    status = models.TextField(choices=STATUS_CHOICES)
    house_type = models.CharField(max_length=50,choices=TYPE_OF_HOUSE)
    size = models.CharField(max_length=50,choices=HOUSE_SIZE)
    
    def __str__(self):
        return f"{self.property_name} - {self.user}"
    
        # start_date = self.start_date = datetime.now()
        # end_date = self.end_date = datetime.now()

    def save(self, *args, **kwargs):
        self.duration = self.end_date - self.start_date
        super().save(*args, **kwargs)

    def __str__(self):
        return self.property_name
    
    # def duration(self):
    #     if self.start_date and self.end_date:
    #         return self.end_date - self.start_date
    #     else:
    #         return None





