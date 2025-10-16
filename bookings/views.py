from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer

from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.action in ["list", "approve", "reject", "destroy", "partial_update", "update"]:
            return [permissions.IsAdminUser()]
        if self.action == "create":
            return [permissions.AllowAny()]
        return [permissions.AllowAny()]

    @action(detail=True, methods=["put"], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk=None):
        booking = self.get_object()
        booking.status = Booking.STATUS_APPROVED
        booking.save()
        return Response(self.get_serializer(booking).data)

    @action(detail=True, methods=["put"], permission_classes=[permissions.IsAdminUser])
    def reject(self, request, pk=None):
        booking = self.get_object()
        booking.status = Booking.STATUS_REJECTED
        booking.save()
        return Response(self.get_serializer(booking).data)


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})