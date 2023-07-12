from django.urls import path

# from . import views
from . import views
from .views import Core_View 
#  tenant_registration_view,
# from Listings_App.views import listing_list

app_name = 'coreApp'

urlpatterns = [
    path('/', Core_View, name= 'main_app'),
    # path('register/', tenant_registration_view, name='tenant_registration'),
    path('api/properties/populate/', views.populate_properties_api), 
]
