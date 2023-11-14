from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from .views import GetUserView, LogoutView, RegisterView


urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('getuser/', GetUserView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', RegisterView.handle_google_login, name='login'),
]