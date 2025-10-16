from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("guest_name", "room", "check_in", "check_out", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("guest_name", "guest_email")
    actions = ["approve_selected", "reject_selected"]

    def approve_selected(self, request, queryset):
        updated = queryset.update(status=Booking.STATUS_APPROVED)
        self.message_user(request, f"{updated} booking(s) approved.")

    def reject_selected(self, request, queryset):
        updated = queryset.update(status=Booking.STATUS_REJECTED)
        self.message_user(request, f"{updated} booking(s) rejected.")

