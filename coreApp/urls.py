from django.urls import path
from coreApp.views import(
    home_view,
    Core_View,
    property_model_list,
    listing_retrieve, 
    listing_create,
    listing_update,
    listing_delete)

app_name = 'coreApp'
urlpatterns = [
    path('', home_view, name ='home'),
    path('main/',Core_View, name ='main'),
    # path('api/properties/populate/', views.populate_properties_api), 
    path('listing/', property_model_list, name ='listing1'),
    path('listing/<pk>/', listing_retrieve, name ='listing2'),
    path('listing/<pk>/delete/', listing_delete, name ='listing3'),
    path('listing_create/', listing_create, name ='listing4'),
    path('listing/<pk>/edit/', listing_update, name='listing_edit')   
]