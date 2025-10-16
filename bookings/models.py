from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from rooms.models import Room

class Booking(models.Model):
    STATUS_PENDING = "pending"
    STATUS_APPROVED = "approved"
    STATUS_REJECTED = "rejected"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        # 1) dates order
        if self.check_in >= self.check_out:
            raise ValidationError("Check-out must be after check-in.")
        # 2) no past check in
        if self.check_in < timezone.localdate():
            raise ValidationError("Check-in cannot be in the past.")
        # 3) overlapping approved bookings (for same room)
        overlapping = Booking.objects.filter(
            room=self.room,
            status=self.STATUS_APPROVED,
            check_in__lt=self.check_out,
            check_out__gt=self.check_in,
        )
        # exclude self when editing
        if self.pk:
            overlapping = overlapping.exclude(pk=self.pk)
        if overlapping.exists():
            raise ValidationError("The room is already booked for the selected dates.")

    def save(self, *args, **kwargs):
        self.full_clean()  # run clean() before saving
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.guest_name} - {self.room.name} ({self.check_in} -> {self.check_out})"
