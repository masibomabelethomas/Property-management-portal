from django.urls import path
from . import views
from . import views  
from coreApp.views import property_model_list, listing_retrive
app_name = 'coreApp'

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('main/', views.Core_View, name = 'main'),
    # path('api/properties/populate/', views.populate_properties_api), 
    path('listing/', property_model_list, name = 'listing'),
    path('listings/<pk>/', listing_retrive, name = 'listings')
]
