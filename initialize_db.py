from app import db, app

# Use the application context
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
