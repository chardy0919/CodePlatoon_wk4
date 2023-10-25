DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS teachers;

CREATE TABLE student(
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    subject INT
);

COPY student from '/home/cody/victor/week_4/Assignments/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject VARCHAR(50)
);

COPY subjects from '/home/cody/victor/week_4/Assignments/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    subject INT
);

COPY teachers from '/home/cody/victor/week_4/Assignments/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;

SELECT * FROM student, subjects, teachers;