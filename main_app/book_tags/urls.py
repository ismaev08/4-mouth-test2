from django.urls import path
from . import views

urlpatterns = [
    path('all_book/', views.all_book, name='all_book'),
    path('kids/', views.kids, name='kids'),
    path('pensioner/', views.pensioner, name='pensioner'),
]