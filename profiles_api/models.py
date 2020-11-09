from django.db import models
# These are the standard base classes that you need to use when overriding or customizing the default Django user model.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
      """Manager for user profiles"""
      def create_user(self, email, name, password=None):
            """Create a new user profile"""
            if not email:
                  raise ValueError('User must have an email address')

            email = self.normalize_email(email)
            user = self.model(email=email, name=name)

            user.set_password(password) # password is encrypted
            user.save(using=self._db)

            return user
      
      def create_superuser(self, email, name, password):
            """Create and save a new superuser with given details"""
            user = self.create_user(email=email, name=name, password=password)

            user.is_superuser = True
            user.is_staff = True

            user.save(using=self._db)

            return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
      """Database model for users in the system"""

      # Every email address in the database must be unique
      email = models.EmailField(max_length=255, unique=True)
      name = models.CharField(max_length=255)
      
      # This is a field that we can use to determine if a user's profile is activated or not. 
      # By default, we are going to set all of them to be activated as True. But, this allows us to deactivate users 
      # if we need at some point in the future.
      is_active = models.BooleanField(default=True)
      # staff user has access to admin interface.
      is_staff = models.BooleanField(default=False)

      # Model Manager that we are going to use for the objects. This is required because we will use our custom UserProfile model
      # with the Django CLI. So, Django needs to have a custom model manager for the UserProfile model, so that it knows how to create users
      # and control the users using the Django command line tools.
      objects = UserProfileManager()

      # When we authenticate users instead of them providing username and password, they are just going to provide email address and password.
      USERNAME_FIELD = 'email'
      # USERNAME_FIELD is required by default. And, then additional required fields specified in REQUIRED_FIELDS
      REQUIRED_FIELDS = ['name']

      def get_full_name(self):
            """Retrieve full name of the user"""
            return self.name
      
      def get_short_name(self):
            """Retrieve short name of the user"""
            return self.name
      
      def __str__(self):
            """Return string representation of our user"""
            return self.email

