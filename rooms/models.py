from django.db import models
from django.urls import reverse
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Tag(AbstractItem):

    """ Tags Model Definition """

    class Meta:
        ordering = ("name",)


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=50)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.PROTECT)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    title = models.CharField(max_length=200)
    creater = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag, related_name="rooms", blank=True)
    upload_user = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE, default=""
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url
