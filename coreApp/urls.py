from django.urls import path
from . import views
from . import views  
from coreApp.views import(
    property_model_list,
      listing_retrive, 
      listing_create,
      listing_update,
      listing_delete
)

app_name = 'coreApp'

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('main/', views.Core_View, name = 'main'),
    # path('api/properties/populate/', views.populate_properties_api), 
    path('listings_list/', property_model_list, name = 'listings_list'),
    path('listing_retrive/<pk>/', listing_retrive, name = 'listing_retrive'),
    path('listing_retrive/<pk>/edit/', listing_update, name = ''),
    path('listing_retrive/<pk>/delete/', listing_delete, name = ''),
    path('add_listing/', listing_create, name = 'add_listing'),
    
]
