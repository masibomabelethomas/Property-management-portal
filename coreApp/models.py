from django.db import models

name = 'coreApp'
 
class Property_model(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    num_rooms = models.PositiveIntegerField()
    AMENITIES_CHOICES = [
        ('Balcony', 'Balcony'),
        ('Gym', 'Gym'),
        ('Swimming Pool', 'Swimming Pool'),
        # Add more amenities as needed
    ]
    amenities = models.TextField(choices=AMENITIES_CHOICES)
  
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES=[
        ('Available','Available'),
        ('Occupied', 'Occupied'),
    ]
    status = models.TextField(choices=STATUS_CHOICES)
    image = models.ImageField()

    def __str__(self):
        return self.name

#Tenant
class Tenant_model(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    property = models.ForeignKey('Property_model', on_delete=models.SET_NULL, blank=True, null=True)
    move_in_date = models.DateField()
    move_out_date = models.DateField(blank=True, null=True)
    references = models.TextField()
    duration = models.DurationField(blank=True, null=True)  # Add the duration field

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.move_in_date and self.move_out_date:
            self.duration = self.move_out_date - self.move_in_date
        super().save(*args, **kwargs)


 #Lease model.
# class Lease_model(models.Model):
#     property = models.ForeignKey('Property_model', on_delete=models.CASCADE)
#     start_date = models.DateField(null=True, blank=True)
#     tenant = models.ForeignKey(Tenant_model, on_delete=models.SET_NULL, blank=True, null=True)
#     end_date = models.DateField()
#     monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
#     security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
#     duration = models.DurationField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.property} - {self.tenant}"

#     def save(self, *args, **kwargs):
#         self.duration = self.end_date - self.start_date
#         super().save(*args, **kwargs)





