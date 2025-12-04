import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-this-secret')
    # Set your MySQL URI like: mysql+pymysql://user:password@localhost/dbname
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:password@localhost/student_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
