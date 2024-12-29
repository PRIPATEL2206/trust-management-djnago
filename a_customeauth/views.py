from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.models import User

from .forms import ProfileUpdateForm

# Create your views here.
@login_not_required
def login_view(request:HttpRequest):

    try:

        if request.POST:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request=request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request=request,message="login successfuly")
                return redirect('/')
            else:
                messages.error(request=request,message="user not found")

    except Exception as e:
        messages.error(request=request,message=str(e))

    return render(request,template_name='customauth/login.html')

@login_not_required
def register_view(request:HttpRequest):

    try:

        if request.POST:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            password1=request.POST.get('password1')
            
            if password==password1:
                user=User.objects.create_user(username,email,password)
                user.save()
                messages.success(request=request,message="register successfuly")
                return redirect("auth_login")
            
            else:
                messages.error(request=request,message="password and conform password must be same")

    except Exception as e:
        messages.error(request=request,message=str(e))

    return render(request,template_name='customauth/register.html')

def logout_view(request:HttpRequest):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect("auth_login")

def profile_view(request:HttpRequest):

    user = request.user
    
    data = {
        'avatar':user.profile.avatar,
        'username':user.username,
        'first_name':user.first_name,                
        'last_name':user.last_name,
        'email':user.email,
        
    }
    form = ProfileUpdateForm(initial=data)
    
    if request.POST:

        form = ProfileUpdateForm(initial=data,data=request.POST,files=request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            user.username = data.get('username')
            user.first_name = data.get('first_name')
            user.last_name = data.get('last_name')
            user.email = data.get('email')
            user.profile.avatar = data.get('avatar')

            user.save()
            user.profile.save()

    return render(request,'customauth/profile_page.html',{'form':form})