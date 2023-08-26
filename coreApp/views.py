from django.shortcuts import render, redirect
from .models import Property_model, Tenant_model
# , Lease_model  
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from .forms import ListingForm

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
    # leases = Lease_model.objects.all()

    context = {
        'properties': properties,
        'tenants': tenants,
        # 'leases': leases,
    }

    return render(request, 'main.html', context)
 

 #crud; create, retrive, update, delete, list,


#the list of the availablwe properties.
def property_model_list(request):
    listings = Property_model.objects.all()

    context = {
        "listings":listings
    }
    return render(request, "listings_list.html", context)


#retriving the properties.

def listing_retrive(request, pk):
    listing = Property_model.objects.get(id=pk)
    context = {
        'listing':listing
    }
    return render (request,"listing_retrive.html", context)

def listing_Create(request):
    form = ListingForm()

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

def listing_update(request):
    
    listing = Property_model.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)