from django.urls import path
from .views import overview, upload, rezepte_main


urlpatterns = [
    path('', overview, name='overview'),
    path('upload/', upload, name='upload'),
    path('rezepte/', rezepte_main, name='rezepte_main')
]
