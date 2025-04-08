# Docker Lab 3: Flask Todo Application

## Overview
In this lab, you'll containerize a Flask-based Todo application with a SQLite database.

## Files Structure
```
flask_todo_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── todo.html
├── config.py
├── run.py
├── requirements.txt
└── README.md
```


### 3. Create Dockerfile

Your task is to create a Dockerfile that:
- Uses an appropriate Python base image
- Installs the required dependencies
- Sets up the Flask application files
- Configures environment variables
- Exposes the correct port 5000 
- use pip install 
- Sets up volume for persistent database storage
- Runs the Flask application when the container starts


## Lab Tasks

1. Create a Dockerfile that containerizes the Flask Todo application
2. Build and run the Docker container
3. Test the application by adding, completing, and deleting todos
4. Verify data persistence by stopping and restarting the container
5. Implement proper environment variable handling

## Advanced Challenges

- Connect to a separate database container (PostgreSQL or MySQL)
- Set up a reverse proxy (Nginx) in front of the Flask application
