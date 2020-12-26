from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Model Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        ("Basic Info", {"fields": ("title", "creater")}),
        ("Tags", {"fields": ("tag",)}),
        ("Uploader", {"fields": ("upload_user",)}),
    )

    list_display = (
        "title",
        "creater",
        "upload_user",
        "tags",
        "count_photos",
        "updated",
    )

    raw_id_fields = ("upload_user",)

    list_filter = ("creater",)

    search_fields = ("=creater", "^tag__name")

    filter_horizontal = ("tag",)

    ordering = (
        "-updated",
        "creater",
    )

    def tags(self, object):
        tags = []
        for tag in object.tag.all():
            tags.append(str(tag))
        return tags

    def count_photos(self, object):
        return object.photos.count()


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):

    """ Tag Admin Model Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Model Definition """

    list_display = ("room", "caption", "see_thumnail")

    ordering = ("room", "caption")

    def see_thumnail(self, object):
        return mark_safe(f'<img width=120px src="{object.file.url}" />')
