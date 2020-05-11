from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, email, name, password=None):
        """create new user profile"""
        if not email:
            raise ValueError('user must have the email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_passwordp[password]
        user.save(using=self._DB)

        return user

    def create_superuser(self, email, name, password):
        """create new superuser profile"""

        user = create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._DB)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    Objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """get user short name"""
        return self.name

    def __str__(self):
        """get email """
        return self.email
