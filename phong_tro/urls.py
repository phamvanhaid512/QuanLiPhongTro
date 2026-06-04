from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from phong_tro.controllers import RoomController


room_controller = RoomController()

urlpatterns = [
    path("rooms/empty/", csrf_exempt(room_controller.empty_rooms)),
    path("rooms/my-rooms/", csrf_exempt(room_controller.my_rooms)),

    path("rooms/", csrf_exempt(room_controller.list)),
    path("rooms/create/", csrf_exempt(room_controller.create)),
    path("rooms/<str:pk>/", csrf_exempt(room_controller.detail)),
    path("rooms/update/<str:pk>/", csrf_exempt(room_controller.update)),
    path("rooms/delete/<str:pk>/", csrf_exempt(room_controller.delete)),
]