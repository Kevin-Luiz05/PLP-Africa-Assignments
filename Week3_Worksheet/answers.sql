-- PLP Africa - Week 3 Day 4 Assignment
-- Student: [Kevin Kamau]
-- File: answers.sql

-- ================================
-- Question 1 🧑‍🎓
-- Create a student table
-- ================================
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 0) -- Ensuring age is always positive
);

-- ================================
-- Question 2 ➕
-- Insert at least 3 records
-- ================================
INSERT INTO student (id, fullName, age) VALUES
(1, 'Alice Johnson', 19),
(2, 'Brian Kamau', 18),
(3, 'Clara Smith', 22);

-- ================================
-- Question 3 🔄
-- Update age of student with ID 2 to 20
-- ================================
UPDATE student
SET age = 20
WHERE id = 2;

-- ================================
-- End of Assignment 🚀
-- ================================
