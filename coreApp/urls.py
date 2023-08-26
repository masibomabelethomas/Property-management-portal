from django.urls import path
from . import views
from . import views  
from coreApp.views import (
    property_model_list,
      listing_retrive, 
      listing_Create,
      listing_update

)

app_name = 'coreApp'

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('main/', views.Core_View, name = 'main'),
    # path('api/properties/populate/', views.populate_properties_api), 
    path('listing_retrive/', property_model_list, name = 'listing_retrive'),
    path('listings_list/<pk>/', listing_retrive, name = 'listings_list/<pk>/'),
    path('add_listing/', listing_Create, name = 'add_listing'),
    path('listing_update/<pk>/edit/', listing_update, name = 'listing_update/<pk>/edit/'),
]
