from rest_framework import viewsets, permissions
from .models import Room
from .serializers import RoomSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404, redirect
from bookings.forms import BookingForm


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    @action(detail=False, methods=["get"])
    def available(self, request):
        qs = self.get_queryset().filter(is_available=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

def rooms_list(request):
    from .models import Room
    rooms = Room.objects.filter(is_available=True)
    return render(request, "rooms_list.html", {"rooms": rooms})

def room_detail(request, pk):
    from .models import Room
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rooms_list")
    else:
        form = BookingForm(initial={"room": room})
    return render(request, "room_detail.html", {"room": room, "form": form})