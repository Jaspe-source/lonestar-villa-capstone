from rest_framework import serializers
from .models import Booking
from datetime import date

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "room", "guest_name", "guest_email", "check_in", "check_out", "status", "created_at"]
        read_only_fields = ["status", "created_at"]

    def validate(self, data):
        check_in = data.get("check_in")
        check_out = data.get("check_out")
        if check_in and check_out:
            if check_in >= check_out:
                raise serializers.ValidationError("Check-out must be after check-in.")
            if check_in < date.today():
                raise serializers.ValidationError("Check-in cannot be in the past.")
        return data
