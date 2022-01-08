from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns=[
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register', register, name='register'),
]