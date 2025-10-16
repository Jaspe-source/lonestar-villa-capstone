from django.urls import path
from . import views

urlpatterns = [
    path("", views.rooms_list, name="rooms_list"),
    path("rooms/<int:pk>/", views.room_detail, name="room_detail"),
]
