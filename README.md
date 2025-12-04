# Student Management System (Flask, MySQL, Bootstrap)
**Complete version** — Authentication, role-based access, CRUD operations for students, marks & attendance, responsive UI.

## Features
- User authentication (Register / Login) with role (admin/faculty/student)
- Add / Edit / Delete student records (CRUD)
- Dashboard with quick stats
- Responsive modern UI (Bootstrap + small custom CSS)
- SQLAlchemy ORM for MySQL (PyMySQL driver)

## Setup (local)
1. Clone or extract the project.
2. Create a Python virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a MySQL database (example):
   ```sql
   CREATE DATABASE student_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
5. Set environment variables (or edit `config.py`):
   ```bash
   export DATABASE_URL='mysql+pymysql://user:password@localhost/student_db'
   export SECRET_KEY='your-secret-key'
   ```
6. Initialize the database:
   ```python
   from app import app, db
   with app.app_context():
       db.create_all()
   ```
7. (Optional) Create an admin user via Python shell or registration page.
8. Run the app:
   ```bash
   python app.py
   ```

## Notes
- This project uses SQLAlchemy and PyMySQL for MySQL connection.
- For production, use a proper WSGI server (gunicorn) and a secure database user.
