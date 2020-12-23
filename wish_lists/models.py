from django.db import models
from core import models as core_models


class WishList(core_models.AbstractTimeStampedModel):

    """ Wish List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="wish_lists", on_delete=models.CASCADE, default=""
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="wish_lists", blank=True)

    def __str__(self):
        return self.name