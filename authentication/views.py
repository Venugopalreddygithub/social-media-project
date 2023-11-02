from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
# Create your views here.


def sign_up_view(request):
    if request.method == "GET":
        return render(request, 'sign_up.html')
     

def sign_in_view(request):
    pass

def sign_out_view(request):
    pass 


