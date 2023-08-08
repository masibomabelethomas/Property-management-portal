from accounts.views import register_view, user_login, user_logout
from django.urls import path


app_name = 'accounts'

urlpatterns = [
path('register/', register_view, name='register'),
path('login/', user_login, name='login'),
path('logout/', user_logout, name='logout'),
]