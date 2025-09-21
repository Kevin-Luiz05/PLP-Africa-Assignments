-- answers.sql
-- PLP Africa — Week 6 Day 4
-- Joins & Relationships assignment
-- Author: <Your Name>
-- Date: YYYY-MM-DD

-- IMPORTANT: Ensure you are using the provided salesdb database
USE salesdb;

-- =====================================================
-- Question 1 🧑‍💼
-- Get firstName, lastName, email, officeCode of all employees
-- Use INNER JOIN between employees and offices on officeCode
-- =====================================================
SELECT
  e.firstName,
  e.lastName,
  e.email,
  e.officeCode
FROM employees AS e
INNER JOIN offices AS o
  ON e.officeCode = o.officeCode
;

-- =====================================================
-- Question 2 🛍️
-- Get productName, productVendor, productLine from products
-- Use LEFT JOIN to include all products even if no matching productline record exists
-- =====================================================
SELECT
  p.productName,
  p.productVendor,
  pl.productLine
FROM products AS p
LEFT JOIN productlines AS pl
  ON p.productLine = pl.productLine
;

-- =====================================================
-- Question 3 📦
-- Retrieve orderDate, shippedDate, status, and customerNumber for the first 10 orders
-- Use RIGHT JOIN to combine customers (left) with orders (right) on customerNumber
-- Order by orderDate ascending and limit to 10 rows (earliest 10 orders)
-- =====================================================
SELECT
  o.orderDate,
  o.shippedDate,
  o.status,
  o.customerNumber
FROM customers AS c
RIGHT JOIN orders AS o
  ON c.customerNumber = o.customerNumber
ORDER BY o.orderDate ASC
LIMIT 10
;
