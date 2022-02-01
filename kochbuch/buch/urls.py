from django.urls import path
from .views import *

urlpatterns = [
    path('', overview, name='overview'),
    path('upload/', upload, name='upload'),
    path('rezepte/', rezepte_main, name='rezepte'),
    path('category/<category_name>', category, name='category'),
    #path('favorites/', favorites, name='favorites'),
   # path('recipe/<recipe_name>', recipe, name='recipe'),
    path('recipe/<int:pk>', RecipeView.as_view(), name='recipe'),
    path('time/', time, name='time'),
    path('filter/', filter_form, name='filter'),
    path('profile/', profile_view, name='profile'),
    path('editprofile/', edit_profile, name='edit_profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('favorite/<int:pk>', AddFavorite, name='add_favorite'),
    path('recipe/<int:pk>/comment', AddComment.as_view(), name='add_comment'),
    path('recipe/<int:pk>/delete_comment', DeleteComment.as_view(), name='delete_comment'),
    path('search', search, name='search'),
    path('recipe/edit/<int:pk>', EditRecipeView.as_view(), name='edit_recipe'),
]
