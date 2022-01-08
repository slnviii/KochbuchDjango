from django.urls import path
from .views import overview, upload, rezepte_main, category, recipe


urlpatterns = [
    path('', overview, name='overview'),
    path('upload/', upload, name='upload'),
    path('rezepte/', rezepte_main, name='rezepte'),
    path('category', category, name='category'),
    path('recipe', recipe, name='recipe'),
]
