-- answers.sql
-- PLP Africa — Week 5 Day 4
-- Database Indexing & Security assignment
-- Author: <Your Name>
-- Date: YYYY-MM-DD

-- =====================================================
-- IMPORTANT: run these as a user with sufficient privileges
-- (e.g., root or an administrative MySQL account).
-- Make sure you are connected to the provided salesdb database.
-- =====================================================

-- Use the specified database (required by the assignment)
USE salesdb;

-- -----------------------
-- Question 1 🗑️
-- Drop index named IdxPhone from customers table.
-- MySQL syntax:
-- Option A (recommended):
ALTER TABLE customers DROP INDEX IdxPhone;
-- Option B (alternate valid syntax):
-- DROP INDEX IdxPhone ON customers;
-- Note: If the index does not exist, these statements will produce an error.
-- You can first inspect with: SHOW INDEX FROM customers;

-- -----------------------
-- Question 2 👤
-- Create a user named 'bob' restricted to localhost with the given password.
-- Use DROP USER IF EXISTS to avoid an error if bob already exists (safe).
DROP USER IF EXISTS 'bob'@'localhost';
CREATE USER 'bob'@'localhost' IDENTIFIED BY 'S$cu3r3!';

-- -----------------------
-- Question 3 🔑
-- Grant the INSERT privilege to bob on the salesDB database.
-- The wildcard *. means all tables in the salesDB database.
GRANT INSERT ON salesDB.* TO 'bob'@'localhost';

-- (Optionally flush privileges — not required for CREATE/GRANT on modern MySQL)
-- FLUSH PRIVILEGES;

-- -----------------------
-- Question 4 🔐
-- Change bob's password to the new password.
-- Modern MySQL (recommended):
ALTER USER 'bob'@'localhost' IDENTIFIED BY 'P$55!23';

-- Alternative (older MySQL versions) if ALTER USER fails:
-- SET PASSWORD FOR 'bob'@'localhost' = PASSWORD('P$55!23');

-- -----------------------
-- Verification queries (optional - run to check results):
-- Show index list for customers
-- SHOW INDEX FROM customers;

-- Show grants for bob
-- SHOW GRANTS FOR 'bob'@'localhost';
