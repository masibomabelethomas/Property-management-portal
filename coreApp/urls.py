from django.urls import path

# from . import views
from . import views
from .views import tenant_registration_view, Core_View

app_name = 'coreApp'

urlpatterns = [
    path('', Core_View, name= 'main_app'),
    path('register/', tenant_registration_view, name='tenant_registration'),
     
]
