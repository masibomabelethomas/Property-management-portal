from django.db import models

name = 'coreApp'
# Create your models here.
#Property
class Property_model(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    num_rooms = models.PositiveIntegerField()
    amenities = models.TextField()
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Tenant
class Tenant_model(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    # lease = models.TextField('Lease_model')
    lease = models.ForeignKey('Lease_model', on_delete=models.SET_NULL, blank=True, null=True)
    # lease = models.ForeignKey('Lease_model', on_delete=models.CASCADE)
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
class Lease_model(models.Model):
    property = models.ForeignKey('Property_model', on_delete=models.CASCADE)
    
    start_date = models.DateField(null=True, blank=True)
    tenant = models.ForeignKey(Tenant_model, on_delete=models.SET_NULL, blank=True, null=True)
    # tenant = models.TextField('Tenant_model')
    # tenant = models.ForeignKey('Tenant_model', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f"{self.property} - {self.tenant}"

    def save(self, *args, **kwargs):
        self.duration = self.end_date - self.start_date
        super().save(*args, **kwargs)

#MaintenanceRequest
class MaintenanceRequest_model(models.Model):
    property = models.ForeignKey('Property_model', on_delete=models.CASCADE)
    tenant = models.ForeignKey('Tenant_model', on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.property} - {self.request_date}"

#Payment.
class Payment_model(models.Model):
    property = models.ForeignKey('Property_model', on_delete=models.CASCADE)
    tenant = models.ForeignKey('Tenant_model', on_delete=models.CASCADE)
    lease = models.ForeignKey('Lease_model', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50, default='pending')
    reference_number = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.property} - {self.payment_date}"

#Invoice.
class Invoice_model(models.Model):
    property = models.ForeignKey('Property_model', on_delete=models.CASCADE)
    tenant = models.ForeignKey('Tenant_model', on_delete=models.CASCADE)
    lease = models.ForeignKey('Lease_model', on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.issue_date}"

