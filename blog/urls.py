from django.urls import path
from . import views

urlpatterns = [
    path('<ink:pk>/', views.single_post_page),
    path('', views.index),
]