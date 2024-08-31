from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    skill_set = db.Column(db.String(120), nullable=False)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))
    required_skill = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(80), default='Assigned')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assign_job', methods=['POST'])
def assign_job():
    data = request.get_json()
    new_job = Job(
        title=data['title'],
        description=data.get('description', ''),
        required_skill=data['required_skill']
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job assigned successfully!'})

@app.route('/get_jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    job_list = [{'title': job.title, 'status': job.status} for job in jobs]
    return jsonify({'jobs': job_list})

# Command to initialize the database
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Database initialized!')

if __name__ == "__main__":
    app.run(debug=True)

