# SportBooking – Sports Facility and Reservation Management System

A web application for managing sports facilities, user accounts, booking time slots, and rating venues.

## 🔧 Features

- User registration and login
- Booking sports facilities for chosen date and time
- Reservation management (create, update, delete)
- User profiles
- Facility ratings (1–5 stars + reviews)
- Admin interface for content management
- REST API built with Django Ninja

---

## 🧰 Technologies Used

- Python 3.11+
- Django 4.x
- SQLite (default database)
- Django Ninja (for REST API)
- Bootstrap 5 (frontend)
- Pydantic 2.x (via Django Ninja)
- Pillow (for image processing)

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/uzivatel/sportsbooking.git
cd sports-booking
```
2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Run migrations**
```bash
python manage.py migrate
```
5. **Create superuser (admin)**
```bash
python manage.py createsuperuser
```
6. **Run server**
```bash
python manage.py runserver
```

🔐 **Admin panel**
```url
http://127.0.0.1:8000/admin
```
![image](https://github.com/user-attachments/assets/60e56584-99d6-49fc-9dde-f97ff9f89c3a)

![image](https://github.com/user-attachments/assets/7e8998d2-74ad-46c5-a4ab-d255b3adef24)

![image](https://github.com/user-attachments/assets/aeb90daa-b068-4518-b888-c95f5f9106c5)


![image](https://github.com/user-attachments/assets/51e5d8bb-115f-438a-9b73-d2c93c80627a)

![image](https://github.com/user-attachments/assets/62578082-e586-4c15-ad24-3cc71cdeb1ba)

