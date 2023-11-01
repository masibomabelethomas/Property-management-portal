from django.shortcuts import render, redirect
from .models import Property_model 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from .forms import ListingForm
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required(login_url='accounts:login')
# @allowed_users(allowed_roles=['Admin', 'Users-Tenants'])
# @admin_only

def home_view(request):
    return render(request, 'accounts/home.html') #index.html

@login_required(login_url='accounts:login')
# @allowed_users(allowed_roles=['Admin','Users-Tenants'])

def Core_View(request):
    properties = Property_model.objects.all()
    context = {
        'properties': properties,  
    }
    return render(request, 'coreApp\templates\main.html', context)

#crud; create, retrive, update, delete, list,
#the list of the available properties.

def property_model_list(request):
    listings = Property_model.objects.all()
    context = {
        "listings":listings
    }
    return render(request, "listings_list.html", context)


#retrieving the properties.
def listing_retrieve(request, pk):
    listing = Property_model.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render (request,"listing_retrieve.html", context)


def listing_create(request):
    form = ListingForm()

    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("coreApp:listing_all")
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

def listing_update(request, pk):
    listing = Property_model.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("coreApp:listing_all")
        
    context = {"form": form}

    return render(request, "listing_update.html", context)

def listing_delete(request, pk):
    listing = Property_model.objects.get(id=pk)
    if request.method == "POST":
        listing.delete()
        return redirect("coreApp:listing_all")
    context ={'listing':listing}
    return render (request, 'delete.html', context)


# bookingViews
# from django.shortcuts import render, redirect
from .bookingforms import BookingForm
from .models import Property_model, Booking

def book_property(request, property_id):
    property = Property_model.objects.get(id=property_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            number_of_guests = form.cleaned_data['number_of_guests']

            # Check if the property is available for the selected dates
            if property.status == 'Available':
                # The property is available; you can create the booking here
                booking = Booking(property=property, check_in_date=check_in_date, check_out_date=check_out_date, number_of_guests=number_of_guests)
                booking.save()
                property.status = 'Occupied'
                property.save()

                # Redirect to a confirmation page or some other success page
                return redirect('coreApp:success_page')
            else:
                # Property is not available
                return redirect('coreApp:property_unavailable')
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form, 'property': property})

def property_unavailable(request):
    return render(request, 'property_unavailable.html')

def success_page(request):
    return render(request, 'success_page.html')
