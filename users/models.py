from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser

class NewUser(AbstractBaseUser):
    """
    New User class extended from AbstractBaseUser
    """
    # translate email address to which language is used by the end user
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # unique identifier we are using for our model
    USERNAME_FIELD = 'email'
    # required field
    REQUIRED_FIELDS  = ['user_name']

    def __str__(self):
        return self.user_name
