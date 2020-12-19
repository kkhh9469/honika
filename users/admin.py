from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Coutom User Admin """

    fieldsets = UserAdmin.fieldsets + (("Avatar", {"fields": ("avatar",)}),)
