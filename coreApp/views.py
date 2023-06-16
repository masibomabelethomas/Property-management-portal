from django.shortcuts import render
from .models import Property_model, Tenant_model, Lease_model, MaintenanceRequest_model, Payment_model, Invoice_model

# Create your views here.
def core_app_view(request):
    properties = Property_model.objects.all()
    tenants = Tenant_model.objects.all()
    leases = Lease_model.objects.all()
    maintenance_requests = MaintenanceRequest_model.objects.all()
    payments = Payment_model.objects.all()
    invoices = Invoice_model.objects.all()

    context = {
        'properties': properties,
        'tenants': tenants,
        'leases': leases,
        'maintenance_requests': maintenance_requests,
        'payments': payments,
        'invoices': invoices,
    }

    return render(request, 'coreApp/core_app.html', context)
