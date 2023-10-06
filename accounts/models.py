from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserAccountManager(BaseUserManager):
    #normal user
    def create_user(self, email, name, phone_number, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        email = email.islower()
        user = self.model(
            email=email,
            name=name,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_realtor(self, email, name, phone_number, password=None):
        user = self.create_user(email, name, phone_number, password)
        user.is_realtor = True
        user.save(using=self.db)
        return user
    
    def create_superuser(self, phone_number, email, name, password=None):
        user = self.create_user(email, name, phone_number, password)
        
        user.is_staff =True
        user.is_superuser=True
        
        user.save(using=self.db)
        return user

class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_realtor = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['name','phone_number']

    def __str__(self):
        return self.email

