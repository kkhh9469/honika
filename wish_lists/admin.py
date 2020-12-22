from django.contrib import admin
from . import models


@admin.register(models.WishList)
class WishListAdmin(admin.ModelAdmin):

    filter_horizontal = ("rooms",)
