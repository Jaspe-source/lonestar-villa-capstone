🏨 Lonestar Villa – Capstone Project

Lonestar Villa is a simple Django + Django REST Framework project for managing hotel rooms and bookings.
It includes both a REST API and a basic web interface.

📁 Project Structure

Main Project: lonestar

Apps: rooms, bookings

API Base URL: /api/

Frontend: Django templates (home, room details, bookings)

⚙️ Features

Manage rooms (name, type, price, description, image, availability)

Create and manage bookings

Admin dashboard for managing all data

REST API endpoints for rooms and bookings

Responsive templates for home, rooms, and bookings

SQLite database (default) with PostgreSQL support for production

Static and media files configured with WhiteNoise

Secure environment variables (SECRET_KEY, DATABASE_URL)

🚀 Quick Setup
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run the server
python manage.py runserver

🌐 Main URLs
Purpose	URL
Home Page	http://127.0.0.1:8000/

Admin Dashboard	http://127.0.0.1:8000/admin/

Rooms API	http://127.0.0.1:8000/api/rooms/

Bookings API	http://127.0.0.1:8000/api/bookings/
🔗 API Endpoints
Endpoint	Method	Description
/api/rooms/	GET	List all rooms
/api/rooms/{id}/	GET	Room details
/api/rooms/available/	GET	Available rooms only
/api/bookings/	GET / POST	List or create bookings
/api/bookings/{id}/approve/	PUT	Approve a booking (admin)
/api/bookings/{id}/reject/	PUT	Reject a booking (admin)
🖼️ UI Pages
Page	Path
Home	/
Room Details	/rooms/<int:pk>/
Bookings List	/bookings/
Admin	/admin/
🧠 Tech Stack

Backend: Django, Django REST Framework

Frontend: Django Templates

Database: SQLite / PostgreSQL

Static Files: WhiteNoise

Deployment Ready: Render compatible

👨‍💻 Author

Jasper Otieno
Capstone Project – Virtual Assistant & Software Development Program

“A home away from home.” 🏡