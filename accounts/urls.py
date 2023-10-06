from .views import user_login, user_logout
# import register_view, user_login, user_logout
from django.urls import path

from .views import RegisterView
# RetrieveUserView
app_name = 'accounts'

urlpatterns = [
    # path('register/', views.register_view, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('get/', RetrieveUserView.as_view()),
]


#classbased views


# urlpatterns = [

# ]



##to be transferred..

        