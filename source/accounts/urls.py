from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import SignUp

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUp.as_view(), name='register'),

]