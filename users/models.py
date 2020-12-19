from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ CustomUserModel """

    avatar = models.ImageField(blank=True)
