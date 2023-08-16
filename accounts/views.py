from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
# from .models import Text, TextForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# @csrf_exempt
def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            password = request.POST.get(make_password('password'))
            user = authenticate(request, user_name=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                # print(user.errors)
                #Handle invalid login
                error_message = "Invalid username or password"
                return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

@csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
        # else:
        #   print(form.errors)
             
            messages.success(request, "Registration Successful")
            return redirect("/")
        messages.error(request, "register.html", {"register_form":form})

    context ={
            "register_form":form,
    }
    return render(request, "register.html", context) 
    
def user_logout(request):
    logout(request)
    return redirect("/")