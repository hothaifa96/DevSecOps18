from app import app, db

# Create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    host = '0.0.0.0'  # Necessary for Docker
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)