from django.shortcuts import render, redirect
from .models import Property_model, Tenant_model, Lease_model, MaintenanceRequest_model, Payment_model, Invoice_model
from .forms import TenantRegistrationForm

# Create your views here.
def Core_View(request):
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

    return render(request, 'core_app.html', context)

# form registration view
def tenant_registration_view(request):
    if request.method == 'POST':
        form = TenantRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after successful registration
    else:
        form = TenantRegistrationForm()

    return render(request, 'registration.html', {'form': form})
