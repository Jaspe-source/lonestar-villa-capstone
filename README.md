# Lonestar Villa - Capstone (Booking System)

Simple Django + DRF project for a hotel/room booking system.

## What's in this repo
- Django project: `lonestar`
- Apps: `rooms`, `bookings`
- API base: `/api/` (router will expose endpoints)

## Quick setup
1. python -m venv venv && source venv/bin/activate
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver

## This week (Week 3)
- Created project skeleton and apps.
- Pushing initial code and this README.

## Next steps (Week 4)
- Implement Room and Booking models + serializers and endpoints.
- Add validations and basic tests.
