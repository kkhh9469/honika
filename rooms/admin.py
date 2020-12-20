from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Model Definition """

    pass


@admin.register(models.Tag)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Model Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin """

    pass