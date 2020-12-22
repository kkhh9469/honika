from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Model Definition """

    fieldsets = (
        ("Basic Info", {"fields": ("title", "creater")}),
        ("Tags", {"fields": ("tag",)}),
        ("Uploader", {"fields": ("upload_user",)}),
    )

    list_display = (
        "title",
        "creater",
        "upload_user",
        "Tags",
    )

    list_filter = ("creater",)

    search_fields = ("=creater", "^tag__name")

    filter_horizontal = ("tag",)

    ordering = ("creater",)

    def Tags(self, object):
        tags = []
        for tag in object.tag.all():
            tags.append(str(tag))
        return tags


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):

    """ Tag Admin Model Definition """


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin """

    pass