from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
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
                image=image,
                user = request.user
            )
            new_post.save()
            messages.success(request, 'Post uploaded successfully!')
            return redirect('all_posts')


    return render(request, 'upload.html')


def Posts(request):
    all_posts = Post.objects.all().order_by('-created_at')

    query = request.GET.get('query')
    if query:
        all_posts = all_posts.filter(title__icontains=query) | all_posts.filter(content__icontains=query)
    data = {'posts': all_posts}
    return render(request, 'posts.html', data)

@login_required(login_url='login')
def Post_details(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=id)
    data = {'post': post, 'comments' :comments}

    if request.method == 'POST' and request.POST.get('comment') is not None:
        content = request.POST.get('comment')
        newComment = Comment.objects.create(post=post, user=request.user, content=content)
        newComment.save()
        messages.success(request, 'Comment Added successfully!')

    if request.method == 'POST' and request.POST.get('liked') is not None:

        isAlreadyLiked = Like.objects.filter(post=post, user=request.user)
        if isAlreadyLiked:
            Like.objects.filter(post=post, user=request.user).delete()
            messages.success(request, 'Liked Deleted successfully!')
        else:
            newLiked = Like.objects.create(post=post, user=request.user)
            newLiked.save()
            messages.success(request, 'Liked Added successfully!')

    return render(request, 'post_detail.html', data) 

@login_required(login_url='login')
def Delete_posts(request, id):
    Post.objects.filter(id=id).delete()
    messages.success(request, 'Post Deleted Successfully!')
    return redirect('my')

@login_required(login_url='login')
def Liked_posts(request):
    all_liked_posts = Like.objects.filter(user=request.user)
    data = {'likedPosts': all_liked_posts}
    return render(request, 'liked.html', data) 

@login_required(login_url='login')
def My(request):
    all_posts = Post.objects.filter(user=request.user).order_by('-created_at')
    data = {'posts': all_posts}
    return render(request, 'my.html', data) 
