from app import app, db

@app.cli.command('init-db')
def init_db():
    with app.app_context():
        db.create_all()
        print('Database initialized!')
