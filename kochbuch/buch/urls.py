from django.urls import path
from .views import overview, upload, rezepte_main, category, recipe, favorites


urlpatterns = [
    path('', overview, name='overview'),
    path('upload/', upload, name='upload'),
    path('rezepte/', rezepte_main, name='rezepte'),
    path('category', category, name='category'),
    path('favorites/', favorites, name='favorites'),
    path('recipe/', recipe, name='recipe'),
]
