from django import forms
from . import models


class SearchForm(forms.Form):

    title = forms.CharField(required=False)
    creater = forms.CharField(required=False)
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class CreatePhotoForm(forms.ModelForm):

    file = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        room = models.Room.objects.get(pk=pk)
        photo.room = room
        photo.save()


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ("title", "creater", "tag")

    def save(self, *args, **kwargs):
        room = super().save(commit=False)
        return room
