from django import forms
from .models import Tenant_model, Lease_model, MaintenanceRequest_model, Payment_model, Invoice_model

class TenantRegistrationForm(forms.ModelForm):
    lease_start_date = forms.DateField(required=False)
    lease_end_date = forms.DateField(required=False)
    monthly_rent = forms.DecimalField(required=False)
    security_deposit = forms.DecimalField(required=False)
    maintenance_request_description = forms.CharField(required=False)
    payment_amount = forms.DecimalField(required=False)

    class Meta:
        model = Tenant_model
        fields = ['name', 'email', 'contact_number']

    def save(self, commit=True):
        tenant = super().save(commit=commit)

        lease_start_date = self.cleaned_data.get('lease_start_date')
        lease_end_date = self.cleaned_data.get('lease_end_date')
        monthly_rent = self.cleaned_data.get('monthly_rent')
        security_deposit = self.cleaned_data.get('security_deposit')
        maintenance_request_description = self.cleaned_data.get('maintenance_request_description')
        payment_amount = self.cleaned_data.get('payment_amount')

        if lease_start_date and lease_end_date and monthly_rent and security_deposit:
            lease = Lease_model.objects.create(
                tenant=tenant,
                start_date=lease_start_date,
                end_date=lease_end_date,
                monthly_rent=monthly_rent,
                security_deposit=security_deposit
            )
            lease.save()

        if maintenance_request_description:
            maintenance_request = MaintenanceRequest_model.objects.create(
                tenant=tenant,
                description=maintenance_request_description
            )
            maintenance_request.save()

        if payment_amount:
            payment = Payment_model.objects.create(
                tenant=tenant,
                amount=payment_amount
            )
            payment.save()

        return tenant
