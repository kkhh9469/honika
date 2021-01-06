from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse


class User(AbstractUser):

    """ CustomUserModel """

    avatar = models.ImageField(upload_to="avatars", blank=True)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
