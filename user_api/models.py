
from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin



class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError("Usuario debe tener un email")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)  

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user 

    

class UserProfile(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length = 100, unique= True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

class HistorialDate(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    init_date = models.DateField()
    end_date = models.DateField()

    

    def __str__(self):
        return self.user.email

    



