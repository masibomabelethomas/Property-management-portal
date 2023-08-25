from django.shortcuts import render, redirect
from .models import Property_model, Tenant_model, Lease_model  
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
# from .forms import TenantRegistrationForm

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['Admin', 'Users-Tenants'])
# @admin_only
def home_view(request):
    return render(request, 'home.html')#index.html

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['Admin'])
def Core_View(request):
    properties = Property_model.objects.all()
    tenants = Tenant_model.objects.all()
    leases = Lease_model.objects.all()

    context = {
        'properties': properties,
        'tenants': tenants,
        'leases': leases,
    }

    return render(request, 'main.html', context)
 

 #crud; create, retrive, update, delete, list,

def property_model_list(request):
    listings = Property_model.objects.all()

    context = {
        "listings":listings
    }
    return render(request, "listings.html", context)

def listing_retrive(request, pk):
    listing = Property_model.objects.get(id=pk)
    context = {
        'listing':listing
    }
    return render (request,"listing.html", context)