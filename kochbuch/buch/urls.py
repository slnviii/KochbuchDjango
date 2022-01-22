from django.urls import path
from .views import overview, upload, rezepte_main, category, recipe, time, filter_form, profile_view


urlpatterns = [
    path('', overview, name='overview'),
    path('upload/', upload, name='upload'),
    path('rezepte/', rezepte_main, name='rezepte'),
    path('category/<category_name>', category, name='category'),
    #path('favorites/', favorites, name='favorites'),
    path('recipe/<recipe_name>', recipe, name='recipe'),
    path('time/', time, name='time'),
    path('filter/', filter_form, name='filter'),
    path('profile/', profile_view, name='profile'),
]
