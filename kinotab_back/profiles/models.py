from django.contrib.auth.models import (AbstractUser, UserManager)
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """User model use email instead username"""

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    receive_offers = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']

    def get_username(self):
        """Return the username for this User."""
        return getattr(self, self.USERNAME_FIELD)

    @property
    def full_name(self):
        return ' '.join((self.first_name, self.last_name))
