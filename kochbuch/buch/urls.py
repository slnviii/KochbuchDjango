from django.urls import path
from .views import overview, upload

urlpatterns=[
    path('', overview),
    path('upload/', upload),
]