from django.urls import path
from . import views
from . import views  
from coreApp.views import(
    property_model_list,
      listing_retrieve, 
      listing_create,
      listing_update,
      listing_delete
)

app_name = 'coreApp'

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('main/', views.Core_View, name = 'main'),
    # path('api/properties/populate/', views.populate_properties_api), 
    path('listings/', property_model_list, name = 'listings'),
    path('listing/<pk>/', listing_retrieve, name = 'listing'),
    # path('listing/<pk>/edit/', listing_update, name = 'listing'),
    path('listing/<pk>/delete/', listing_delete, name = 'listing'),
    path('listing/', listing_create, name = 'listing'),
    path('listing/<int:pk>/edit/', listing_update, name='listing_edit')

    
]
