from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.Posts, name='all_posts'),
    path('upload/', views.Upload, name='uploads'),
    path('<int:id>/', views.Post_details, name='post_detail'),
    path('likes/', views.Liked_posts, name='likes'),
    path('my/', views.My, name='my'),
    path('delete/<int:id>/', views.Delete_posts, name='delete_post'),
] 
