import os

# Get the folder where this file is located
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the SQLite database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'instance', 'todo.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configure secret key
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# Debug mode
DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'