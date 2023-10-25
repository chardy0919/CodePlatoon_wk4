DROP TABLE IF EXISTS students;

-- Create the students table
CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade CHAR(1)
);

-- Insert student data
INSERT INTO students (first_name, last_name, age, grade) VALUES
    ('John', 'Doe', 18, 'A'),
    ('Jane', 'Smith', 19, 'B'),
    ('Bob', 'Johnson', 20, 'C'),
    ('Emily', 'Williams', 18, 'A'),
    ('Samantha', 'Davis', 22, 'A'),
    ('Michael', 'Brown', 19, 'B'),
    ('Oliver', 'Jones', 20, 'B'),
    ('Sophia', 'Miller', 21, 'A'), 
    ('Ethan', 'Wilson', 19, 'C'), 
    ('Isabella', 'Moore',22, 'B');
 
-- Retrieve student information
SELECT * FROM students;