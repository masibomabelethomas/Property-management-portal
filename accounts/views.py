from django.shortcuts import render, redirect 
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


# def landing_page(request):
#     return render(request, 'templates/commons/header.html')

#our login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            user = authenticate(request, user_name=user_name, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'username or password is incorrect')
        # context = {}
        return render(request, 'login.html')

# Create your views here.
def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration Successful")
            return redirect("/")
        messages.error(request, "register.html", {"register_form":form})

    context ={
            "register_form":form,
    }

    return render(request, "register.html", context) 
    # 

def user_logout(request):
    logout(request)
    return redirect('/')