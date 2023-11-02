from django.urls import path 
from authentication.views import sign_up_view, sign_in_view, sign_out_view 

urlpatterns = [
    path('sign-up/', sign_up_view, name='sign_up_view'),
    path('sign-in/', sign_in_view, name='sign_in_view'),
    path('sign-out/', sign_out_view, name='sign_out_view'),
    
]
