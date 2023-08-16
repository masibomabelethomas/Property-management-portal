from django.urls import path
from . import views
from . import views  

app_name = 'coreApp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('main/', views.Core_View, name= 'main'),
    path('api/properties/populate/', views.populate_properties_api), 
]
