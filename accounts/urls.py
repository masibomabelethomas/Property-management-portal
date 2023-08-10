from accounts.views import register_view, user_login, user_logout
from django.urls import path
# from .views import landing_page

app_name = 'accounts'

urlpatterns = [

    # path('', landing_page, name= 'header'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/login/', user_login, name='login'),
    path('accounts/logout/', user_logout, name='logout'),
]