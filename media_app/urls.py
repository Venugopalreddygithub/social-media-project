from django.urls import path 
from media_app.views import index_view, submit_post, like_post, profile_view, upload_profile
# upload_profile

urlpatterns = [
    path('', index_view, name='index'),
    path('submit-post/', submit_post, name='submit_post'),
    path('like-post/<int:post_id>/', like_post, name='like_post'),
    path('profile-view/<str:username>/', profile_view, name='profile_view'),
    path('upload-profile/', upload_profile, name='upload_profile'),
]
