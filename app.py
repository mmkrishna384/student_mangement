import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm, StudentForm
from models import db, User, Student
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # create user
        user = User(name=form.name.data, email=form.email.data, role=form.role.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    # simple stats
    total = Student.query.count()
    return render_template('dashboard.html', total=total)

@app.route('/students')
@login_required
def students():
    students = Student.query.order_by(Student.id.desc()).all()
    return render_template('students.html', students=students)

@app.route('/students/add', methods=['GET','POST'])
@login_required
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        s = Student(name=form.name.data, roll_no=form.roll_no.data, email=form.email.data,
                    marks=form.marks.data, attendance=form.attendance.data)
        db.session.add(s)
        db.session.commit()
        flash('Student added successfully.', 'success')
        return redirect(url_for('students'))
    return render_template('add_student.html', form=form)

@app.route('/students/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_student(id):
    s = Student.query.get_or_404(id)
    form = StudentForm(obj=s)
    if form.validate_on_submit():
        form.populate_obj(s)
        db.session.commit()
        flash('Student updated.', 'success')
        return redirect(url_for('students'))
    return render_template('edit_student.html', form=form, student=s)

@app.route('/students/delete/<int:id>', methods=['POST'])
@login_required
def delete_student(id):
    s = Student.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    flash('Student removed.', 'success')
    return redirect(url_for('students'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
