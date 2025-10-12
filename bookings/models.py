from django.db import models
from django.utils import timezone
from rooms.models import Room

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking for {self.guest_name} in {self.room.name}"

    class Meta:
        ordering = ['-created_at']

