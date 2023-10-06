from django.shortcuts import render, redirect, get_object_or_404

# from .import RegisterForm
# from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user  # this function is defined in the decorators file to make this code section clean.
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")

        user = authenticate(username=user_name, password=password)

        if user is not None:
            login(request, user)
            return redirect("coreApp:home")
            # print(user.error)
        else:
            messages.info(request, "Invalid Username or Password")
            # Handle invalid login
    context = {}
    return render(request, "accounts/login.html", context)


# @csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
# def register_view(request):
#     if request.user.is_authenticated:
#          return redirect('home')
#     else:
#         form = RegisterForm()
#         if request.method == "POST":
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 username = form.cleaned_data.get('username')

#                 group = Group.objects.get(name='Users-Tenants')
#                 user.group.add(group)

#                 messages.success(request, "Registration Successful for " + username)
#                 return redirect("accounts:login")

#         context ={"register_form":form,}
#         return render(request, "register.html", context)


def user_logout(request):
    logout(request)
    return redirect("accounts:login")


# class based views for registering users
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.views import APIView 
from django.views.generic import TemplateView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()
# from .forms import RegisterForm
from rest_framework.permissions import IsAuthenticated
from .serializers import Userserializers


class RegisterView(TemplateView):
    template_name = 'accounts/register.html'
#     permission_classes = [permissions.AllowAny]
    # permission_classes = [IsAuthenticated]
    def post(self,request, *args, **kwargs):
        if request.method =='POST':
          #   data = request.data
            email=request.POST.get('email')
            name=request.POST.get('name')
            password=request.POST.get('password')
            re_password=request.POST.get('re_password')
            phone_number=request.POST.get('phone_number')
            user=User.objects.create(name=name,email=email,password=password,phone_number=phone_number)
            return redirect('coreApp:home')
        




# class RegisterView(TemplateView):
#     template_name = 'accounts/register.html'
#     permission_classes = [permissions.AllowAny]
#     # permission_classes = [IsAuthenticated]
#     def post(self, request):
        
#         if request.user.is_authenticated:
#             return redirect("home")
#         else:
#             # defining the form
#             form = RegisterForm(self, request.POST)
#             if form.is_valid():
#                 ##
#                 try:
#                     data = request.data
#                     name = data["name"]
#                     email = data["email"]
#                     email = email.lower()
#                     # phone_number = data["phone_number"]
#                     password = data["password"]
#                     re_password = data["re_password"]
#                     is_realtor = data["is_realtor"]
#                     if is_realtor == "True":
#                         is_realtor = True
#                     else:
#                         is_realtor = False
#                     if password == re_password:
#                         if len(password) >= 8:
#                             if not User.objects.filter(email=email).exists():
#                                 if not is_realtor:
#                                     User.objects.create_user(
#                                         name=name,
#                                         email=email,
#                                         password=password,
#                                         # phone_number=phone_number,
#                                     )
#                                     return Response(
#                                         {"success": "User created successfully"},
#                                         status=status.HTTP_201_CREATED,
#                                     )
#                                 else:
#                                     User.objects.create_realtor(
#                                         name=name,
#                                         email=email,
#                                         password=password,
#                                         # phone_number=phone_number,
#                                    print('kuja')
#                                     )
#                                     return Response(
#                                         {
#                                             "success": "Realtor account created successfully"
#                                         },
#                                         status=status.HTTP_201_CREATED,
#                                     )

#                                 return Response(
#                                     {"error": "user with this email already exist"},
#                                     status=status.HTTP_400_BAD_REQUEST,
#                                 )

#                             else:
#                                 return Response(
#                                     {
#                                         "error": "password should be atleast 8 characters length"
#                                     },
#                                     status=status.HTTP_400_BAD_REQUEST,
#                                 )

#                     else:
#                         return Response(
#                             {"error": "password do not match"},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                         )
#                 except:
#                     return Response(
#                         {"error": "something went wrong when registering an account"},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                     )
#             else:
#                 form = RegisterForm()

#             context = {"register_form": form}
#             return render(request, "register.html", context)




# classed based view for retriving users

# class RetrieveUserView(APIView):
#      def get(self, request, format=None):
#           try:
#                user = request.user
#                user = Userserializers(user)

#                return Response(
#                     {'user': user.data},
#                     status = status.HTTP_200_OK
#                )

#           except:
#                 return Response(
#                     {'error':'something went wrong when retriving user details'},
#                     status=status.HTTP_500_INTERNAL_SERVER_ERROR
#                )
