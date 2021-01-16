import os
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from users import mixins as user_mixins
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 5
    paginate_orphans = 2
    context_object_name = "rooms"
    ordering = ("-created",)


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


class SerchView(View):
    def get(self, request):
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            creater = form.cleaned_data.get("creater")
            tags = form.cleaned_data.get("tags")

            filter_args = {}

            if title is not None:
                filter_args["title__icontains"] = title

            if creater is not None:
                filter_args["creater__icontains"] = creater

            for tag in tags:
                filter_args["tag"] = tag

            rooms = models.Room.objects.filter(**filter_args)
            rooms = reversed(rooms)

            # To do
            # paginiate 제한, page nav 만들기

        return render(
            request,
            "rooms/search.html",
            {"form": form, "rooms": rooms},
        )


class EditRoomView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Room
    fields = (
        "title",
        "creater",
        "tag",
    )
    template_name = "rooms/room_edit.html"

    def get_success_url(self):
        upload_user_pk = self.object.upload_user.pk
        return reverse("users:profile", args=[upload_user_pk])

    def get_object(self, quryset=None):
        room = super().get_object(queryset=quryset)
        if room.upload_user.pk != self.request.user.pk:
            raise Http404()
        return room


class RoomPhotosView(user_mixins.LoggedInOnlyView, DetailView):

    model = models.Room
    template_name = "rooms/room_photos.html"

    def get_object(self, quryset=None):
        room = super().get_object(queryset=quryset)
        if room.upload_user.pk != self.request.user.pk:
            raise Http404()
        return room


@login_required
def delete_photo(request, room_pk, photo_pk):
    user = request.user
    try:
        room = models.Room.objects.get(pk=room_pk)
        if room.upload_user.pk != user.pk:
            messages.error(request, "이미지를 지울 수 없습니다")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
        return redirect(reverse("rooms:photos", kwargs={"pk": room_pk}))
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))


class EditPhotoView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Photo
    template_name = "rooms/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    fields = ("caption",)

    def get_success_url(self):
        room_pk = self.kwargs.get("room_pk")
        return reverse("rooms:photos", kwargs={"pk": room_pk})


class AddPhotoView(user_mixins.LoggedInOnlyView, FormView):

    model = models.Photo
    template_name = "rooms/photo_create.html"
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        # form.save_m2m() 다중 업로드 구현하기
        return redirect(reverse("rooms:photos", kwargs={"pk": pk}))


class CreateRoomView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateRoomForm
    template_name = "rooms/room_create.html"

    def form_valid(self, form):
        room = form.save()
        room.upload_user = self.request.user
        room.save()
        form.save_m2m()
        return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))