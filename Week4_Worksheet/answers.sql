-- answers.sql
-- PLP Africa - Week 4, Day 4
-- Advanced SQL Queries & Aggregations
-- Author: <Your Name>
-- Date: YYYY-MM-DD

/*************************************************************
 Question 1
 Show total payment amount for each paymentDate (descending)
 and display only the top 5 latest payment dates.
*************************************************************/

-- MySQL / PostgreSQL version (use this if you are on MySQL/Postgres)
SELECT
  paymentDate,
  SUM(amount) AS total_amount
FROM payments
GROUP BY paymentDate
ORDER BY paymentDate DESC
LIMIT 5;

-- SQL Server version (if you use MS SQL Server, use this variant)
-- SELECT TOP 5
--   paymentDate,
--   SUM(amount) AS total_amount
-- FROM payments
-- GROUP BY paymentDate
-- ORDER BY paymentDate DESC;


/*************************************************************
 Question 2
 Find the average credit limit of each customer.
 Display: customer name, country, average credit limit.
 Group by customer name and country.
*************************************************************/

SELECT
  customerName,
  country,
  AVG(creditLimit) AS avg_credit_limit
FROM customers
GROUP BY customerName, country;

/*************************************************************
 Question 3
 Find total price of products ordered from orderdetails.
 Option A (recommended): aggregate per product across all orders:
   - productCode
   - total_quantity_ordered
   - total_price (sum of quantityOrdered * priceEach)
 Group by productCode.
*************************************************************/

SELECT
  productCode,
  SUM(quantityOrdered) AS total_quantity_ordered,
  SUM(quantityOrdered * priceEach) AS total_price
FROM orderdetails
GROUP BY productCode
ORDER BY total_price DESC;

-- Option B (if your instructor expects grouping by product code AND quantityOrdered
-- exactly as worded in the brief, use this variant instead):
-- SELECT
--   productCode,
--   quantityOrdered,
--   SUM(quantityOrdered * priceEach) AS total_price
-- FROM orderdetails
-- GROUP BY productCode, quantityOrdered
-- ORDER BY productCode, quantityOrdered;


/*************************************************************
 Question 4
 Find highest payment amount for each checkNumber.
 Display: checkNumber and highest amount.
 Group by checkNumber.
*************************************************************/

SELECT
  checkNumber,
  MAX(amount) AS highest_amount
FROM payments
GROUP BY checkNumber;
