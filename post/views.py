from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages

# Create your views here.
def Upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        visibility = request.POST.get('visibility')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        if not title or not content or not author:
            messages.error(request, 'Please fill in all required fields.')
            return redirect ('uploads')
        else:
            new_post = Post(
                title=title,
                content=content,
                author=author,
                visibility=visibility,
                category=category,
                image=image
            )
            new_post.save()
            messages.success(request, 'Post uploaded successfully!')
            return redirect('all_posts')


    return render(request, 'upload.html')

def Posts(request):
    return render(request, 'posts.html')
