from django.urls import path
from . import views

urlpatterns = [
    path('' , views.book_list_view, name='books'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('about/', views.about_me, name='about'),
    path('pets/', views.about_pets, name='pets'),
    path('time/', views.system_time, name='time'),
]





# urlpattern = [
#     path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
#     path('', views.books, name='books'),
#     path('about/', views.about_me, name='about'),
#     path('pets/', views.index, name='pets'),
#     path('time/', views.system_time, name='time'),
# ]
