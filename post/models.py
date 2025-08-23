from django.db import models
from django.contrib.auth.models import User
# Post model
class Post(models.Model):

    visibility_choices = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    category_choices = [
        ('tech', 'Technology'),
        ('life', 'Lifestyle'),
        ('edu', 'Education'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=10, choices=visibility_choices, default='public')
    category = models.CharField(max_length=10, choices=category_choices, default='other')
    likes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
    
# Comment model    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'
    
# Like model
class Like(models.Model):
    post = models.ForeignKey(Post, related_name='like_posts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='like_users', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'Like by {self.user.username} on {self.post.title}'
    
    
