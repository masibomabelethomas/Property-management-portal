from django.urls import path
from . import views
app_name = 'coreApp'

urlpatterns = [
    path('', views.Core_View),
    # path('main/', views.Core_View, name='main'),
     
]
