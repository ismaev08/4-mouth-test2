from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('ingredient/add/<int:recipe_id>/', views.add_ingredient, name='add_ingredient'),
    path('ingredient/edit/<int:ingredient_id>/', views.edit_ingredient, name='edit_ingredient'),
    path('recipe/delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('collection/<int:pk>/', views.collection_detail, name='collection_detail'),
]
