from app import app

with app.app_context():
    print('App context is working!')
