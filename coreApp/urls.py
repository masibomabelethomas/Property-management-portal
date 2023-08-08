from django.urls import path

# from . import views
from . import views
from .views import Core_View #main_app
from .views import home_view
#  tenant_registration_view,
# from Listings_App.views import listing_list

app_name = 'coreApp'

urlpatterns = [

    path('', views.home_view, name='home'),
    path('main/', views.Core_View, name= 'main'),
    # path('register/', tenant_registration_view, name='tenant_registration'),
    path('api/properties/populate/', views.populate_properties_api), 
]
