from flask import Flask, jsonify
students = [
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
    {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
    {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
    {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
    {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
    {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
    {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
    {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
]

app = Flask(__name__)

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    oldies = []
    for student in students:
        if student["age"] > 20:
            oldies.append(student)
    return jsonify(oldies)

@app.route('/young_students', methods=['GET'])
def get_young_students():
    yungins = []
    for student in students:
        if student["age"] < 21:
            yungins.append(student)
    return jsonify(yungins)

@app.route('/advance_students', methods=['GET'])
def get_advance_students():
    smarty = []
    for student in students:
        if student["age"] < 21 and student['grade'] == "A":
            smarty.append(student)
    return jsonify(smarty)

@app.route('/names_students', methods=['GET'])
def get_names_students():
    names = [{'f_name': student['first_name'], 'l_name': student['last_name']} for student in students]
    return jsonify(names)

@app.route('/ages_students', methods=['GET'])
def get_ages_students():
    ages = [{'name': student['first_name']+ ' ' +student['last_name'], 'age': student['age']} for student in students]
    return jsonify(ages)



if __name__ == '__main__':
    app.run(debug=True)