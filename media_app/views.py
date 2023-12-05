from django.shortcuts import render, redirect 
from media_app.models import Post, LikePost, Profile
from authentication.models import User 
from django.contrib.auth.decorators import login_required 

# Create your views here.
def index_view(request):
    page_name = 'index.html'
    data = {
        "posts" : Post.objects.all().order_by('-created_at')
    }
    return render(request, page_name, data)


@login_required(login_url='sign_in_view')
def submit_post(request):
    user = request.user 
    content = request.POST['post_caption']
    image = request.FILES.get('post_image')
    Post.objects.create(
        user=user,
        caption=content,
        image=image,
    )
    
    return redirect('index')

@login_required(login_url='sign_in_view')
def like_post(request, post_id):
    user = request.user 
    post = Post.objects.get(id=post_id)
    LikePost.objects.create(
        user=user,
        post=post,
    )
    
    return redirect('index')

@login_required(login_url='sign_in_view')
def profile_view(request, username):
    user = User.objects.get(username=username)
    posts_made = user.post.all().count()
    likes_made = user.like_post.all().count()
    likes_received = LikePost.objects.filter(post__user=user).count()
    data = {
        "user": user,
        "posts_made": posts_made,
        "likes_made": likes_made,
        "likes_received": likes_received,
    }
    
    return render(request, 'profile.html', data)

@login_required(login_url='sign_in_view')
def upload_profile(request):
    user = request.user
    image = request.FILES.get('profile_image')
    profile = Profile.objects.get(user=user)
    profile.image = image 
    profile.save()
    return redirect(f'/profile-view/{user.username}')