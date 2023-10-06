# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()

# class RegisterForm(UserCreationForm):
#     email =forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('name','email','password','phone_number','re_password')

    # def save(self, commit=True):
    #     user = super(RegisterForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.phone_number = self.cleaned_data['phone_number']
    #     user.re_password = self.cleaned_data['re_password']
    #     if commit:
    #         user.save()
    #         return user