from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.Posts, name='all_posts'),
    path('upload/', views.Upload, name='uploads'),
]
