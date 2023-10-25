from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///students2'
db = SQLAlchemy(app)
class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    student_list = [
        {'id': student.id, 
         'first_name': student.first_name, 
         'last_name': student.last_name, 
         'age': student.age, 
         'grade': student.grade} 
         for student in students
    ]
    return jsonify(student_list)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    students = Students.query.filter(Students.age > 20)
    student_list = [
        {'id': student.id, 
         'first_name': student.first_name, 
         'last_name': student.last_name, 
         'age': student.age, 
         'grade': student.grade} 
         for student in students
    ]
    return jsonify(student_list)

@app.route('/young_students', methods=['GET'])
def get_young_students():
    students = Students.query.filter(Students.age < 21)
    student_list = [
        {'id': student.id, 
         'first_name': student.first_name, 
         'last_name': student.last_name, 
         'age': student.age, 
         'grade': student.grade} 
         for student in students
    ]
    return jsonify(student_list)

@app.route('/smart_students', methods=['GET'])
def get_smart_students():
    students = Students.query.filter(Students.grade == 'A', Students.age < 21)
    student_list = [
        {'id': student.id, 
         'first_name': student.first_name, 
         'last_name': student.last_name, 
         'age': student.age, 
         'grade': student.grade} 
         for student in students
    ]
    return jsonify(student_list)

@app.route('/name_students', methods=['GET'])
def get_name_students():
    students = Students.query.all()
    student_list = [
        {
         'name': student.first_name+ " " +student.last_name, 
         'age': student.age, 
         } 
         for student in students
    ]
    return jsonify(student_list)

if __name__ == '__main__':
    app.run(debug = True)