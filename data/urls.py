from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload_file, name="test_upload"),
    path('test/<int:id>/', get_test, name="test")
]