from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page_size = 10

    # 장고 어시스트
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, page_size)
    rooms = paginator.get_page(page)

    # Room 뒤집기
    page = int(page)
    limit = page_size * page
    offest = limit - page_size
    reversed_rooms = reversed(models.Room.objects.get_queryset())
    lastest_rooms = []
    for room in reversed_rooms:
        lastest_rooms.append(room)
    all_rooms = lastest_rooms[offest:limit]

    return render(
        request,
        "rooms/home.html",
        context={"page": rooms, "lastset_rooms": all_rooms},
    )
