from django.shortcuts import render, redirect 
from media_app.models import Post, LikePost
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