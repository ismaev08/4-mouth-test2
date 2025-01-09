from . import views
from django.urls import path

urlpatterns = [
   path('', views.index),
   path('about_me', views.about_me),
   path('time/', views.system_time, name='time'),
]