from django.shortcuts import render, redirect
from .models import Property_model, Tenant_model, Lease_model, MaintenanceRequest_model, Payment_model, Invoice_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# from .forms import TenantRegistrationForm

# Create your views here.
# accounts/views.py (or another app's views.py)
 
def home_view(request):
    return render(request, 'home.html')#index.html

# @login_required
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

    return render(request, 'main.html', context)

# form registration view
# def tenant_registration_view(request):
#     if request.method == 'POST':
#         form = TenantRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Redirect to a success page after successful registration
#     else:
#         form = TenantRegistrationForm()

#     return render(request, 'registration.html', {'form': form})


#populate data api
from django.http import JsonResponse
from .models import Property_model

def populate_properties_api(request):
    # Make a request to another API or use data from a different source
    property_data = [
        {
        'name': 'Property 1',
        'address': '123 Main St',
        'size': 1200,
        'num_rooms': 3,
        'amenities': 'Swimming pool, Gym, Parking',
        'rental_price': 1500.00,
        'status': 'Available',
    },
    {
        'name': 'Property 2',
        'address': '456 Elm St',
        'size': 1000,
        'num_rooms': 2,
        'amenities': 'Garden, Balcony',
        'rental_price': 1200.00,
        'status': 'Occupied',
    }, 
    ]
    for data in property_data:
        property_instance = Property_model(
            name=data['name'],
            address=data['address'],
            size=data['size'],
            num_rooms=data['num_rooms'],
            amenities=data['amenities'],
            rental_price=data['rental_price'],
            status=data['status'],
        )
            # Set other attributes based on the property data
        
        property_instance.save()
    return JsonResponse({'message': 'Properties populated successfully'})
