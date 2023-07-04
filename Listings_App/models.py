# from django.db import models

# # Create your models here.
# class Listing_model(models.Model):
#     title = models.CharField(max_length=255)
#     rental_price = models.DecimalField(max_digits=10, decimal_places=2)
#     num_rooms = models.PositiveIntegerField()
#     size = models.PositiveIntegerField()
#     address = models.CharField(max_length=255)
#     AMENITIES_CHOICES = [
#         ('balcony', 'Balcony'),
#         ('gym', 'Gym'),
#         ('pool', 'Swimming Pool'),
#         # Add more amenities as needed
#     ]
#     amenities = models.TextField(choices=AMENITIES_CHOICES)
    
    
#     status = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title