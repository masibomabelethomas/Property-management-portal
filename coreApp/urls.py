from django.urls import path
from coreApp.views import(
    home_view,
    Core_View,
    property_model_list,
    listing_retrieve, 
    listing_create,
    listing_update,
    listing_delete,
    book_property)

app_name = 'coreApp'

urlpatterns = [
    path('', home_view, name ='home'),
    path('main/',Core_View, name ='main'),

    # path('api/properties/populate/', views.populate_properties_api), 
    path('create_listing/', listing_create, name ='create_listing'),

    path('listing_all/', property_model_list, name ='listing_all'),

    path('retrieve_listing/<int:pk>/', listing_retrieve, name ='retrieve_listing'),

    path('delete_listing/<int:pk>/', listing_delete, name ='delete_listing'),
    path('update_listing/<int:pk>/', listing_update, name='update_listing'),

    path('book_property/<int:property_id>/', book_property, name='book_property'),
]