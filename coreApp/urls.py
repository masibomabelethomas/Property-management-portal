from django.urls import path
from .views import core_app_view

urlpatterns = [
    path('coreApp/', core_app_view.core, name='core'),
    # path('core/', core_app_view, name='core_App.urls'),
]
