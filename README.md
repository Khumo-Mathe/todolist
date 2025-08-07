📝 Django Todo List App
A simple yet fully functional Todo List web application built with Django. This project allows users to register, log in, and manage their personal tasks. Tasks can be added, updated, marked as complete, or deleted. The app includes basic authentication, form handling, and a styled HTML/CSS frontend.

🔧 Features
✅ User Registration & Login

✅ Add, Update, and Delete Tasks

✅ Mark Tasks as Complete/Incomplete

✅ View Only Your Own Tasks (per user)

✅ Basic UI with HTML & CSS

✅ Secure with Django Authentication System

🚀 Tech Stack
Backend: Django (Python)

Frontend: HTML5, CSS3

Database: SQLite3

Authentication: Django’s built-in auth system

📂 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/todolist.git
cd todolist
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/Scripts/activate  # or venv\Scripts\activate for Windows
Install dependencies:

bash
Copy
Edit
pip install django
Run migrations:

bash
Copy
Edit
python manage.py migrate
Create superuser:

bash
Copy
Edit
python manage.py createsuperuser
Run the server:

bash
Copy
Edit
python manage.py runserver
Open in browser:

cpp
Copy
Edit
http://127.0.0.1:8000/
