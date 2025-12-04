from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('admin','Admin'), ('faculty','Faculty'), ('student','Student')], default='faculty')
    submit = SubmitField('Register')

class StudentForm(FlaskForm):
    roll_no = StringField('Roll Number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    marks = IntegerField('Marks', validators=[DataRequired()])
    attendance = FloatField('Attendance (in %)', validators=[DataRequired()])
    submit = SubmitField('Save')
