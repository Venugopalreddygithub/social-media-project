from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from authentication.models import User 
from django.contrib.auth.models import auth 
from media_app.models import Profile 
# Create your views here.


def sign_up_view(request):
    page_name="sign_up.html"
    if request.method == "GET":
        print(request.user)
        print(request.user.is_authenticated)
        
        return render(request, 'sign_up.html')
    else: #POST 
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if email == '' :
            return render(request, page_name, context={"error": True, "error_msg": "Email is required"})  
        
        if username == '' :
            return render(request, page_name, context={"error": True, "error_msg": "username is required"})  
        
        if password == '':
            return render(request, page_name, context={"error": True, "error_msg": "password is required"})   
        
        if User.objects.filter(username=username).exists():
            return render(request, page_name, context={"error": True, "error_msg": "Username already exists"})   
         
        if User.objects.filter(email=email).exists():
            return render(request, page_name, context={"error": True, "error_msg": "Email already exists"}) 
        
        User.objects.create_user(username=username, password=password, email=email)
        user = auth.authenticate(username=username, password=password)
        Profile.objects.get_or_create(user=user)
        auth.login(request, user)
        return render(request, page_name)
 
def sign_in_view(request):
    if request.method == "GET":
        return render(request, 'sign_in.html')

def sign_out_view(request):
    pass 


