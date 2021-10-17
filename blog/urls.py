from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<ink:pk>/', views.single_post_page),
    #path('', views.index),
    #path('', include('single_pages.url')),
]