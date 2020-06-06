from django.contrib.auth.models import (AbstractBaseUser)
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser):
    """User model use email instead username"""
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_username(self):
        """Return the username for this User."""
        return getattr(self, self.USERNAME_FIELD)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)

    @property
    def full_name(self):
        return ' '.join((self.first_name, self.last_name))
