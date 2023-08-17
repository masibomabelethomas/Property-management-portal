from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt,csrf_protect

@csrf_exempt
def user_login(request):
    if request.user.is_authenticated:
         return redirect('home')
    else:
        if request.method == 'POST':
                user_name = request.POST.get('user_name')
                password = request.POST.get('password')

                user = authenticate(request, user_name=user_name, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect ('home')
                else:
                    messages.info(request,'Invalid Username or Password')
                    #Handle invalid login 
        context = {}
        return render(request, 'login.html', context)

# @csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
def register_view(request):
    if request.user.is_authenticated:
         return redirect('home')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')

                messages.success(request, "Registration Successful for " + user)
                return redirect("accounts:login")

        context ={"register_form":form}
        return render(request, "register.html", context) 


def user_logout(request):
    logout(request)
    return redirect("accounts:login")