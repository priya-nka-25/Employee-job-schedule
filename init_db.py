from app import app, db  # Import your app and db from the application

def init_db():
    with app.app_context():  # Create an application context
        db.create_all()
        print('Database initialized!')

if __name__ == '__main__':
    init_db()
