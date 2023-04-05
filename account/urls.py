from django.urls import path
from .views import home, RegisterView, login_view

urlpatterns = [
    path("home/", home, name="home"),
    path('register/',RegisterView.as_view(), name='reg'),
    path('login/', login_view, name="login")
]