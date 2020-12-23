from django.contrib import admin
from . import models


@admin.register(models.WishList)
class WishListAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "see_lists",
    )
    filter_horizontal = ("rooms",)

    ordering = ("name",)

    def see_lists(self, object):
        lists = []
        for see_list in object.rooms.all():
            lists.append(str(see_list))
        return lists
