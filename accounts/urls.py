from .views import register_view, user_login, user_logout
from django.urls import path
 
app_name = 'accounts'

urlpatterns = [
    # path('register/', views.register_view, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register_view, name='register'),
    # path('get/', RetrieveUserView.as_view()),
]
 
        