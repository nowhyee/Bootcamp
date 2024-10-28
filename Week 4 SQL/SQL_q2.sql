/* Pull total number of customers that purchased in January 2023 and the average amount spend per customer*/
SELECT COUNT(DISTINCT Customer_id) AS total_customers, AVG(Revenue) AS avg_spent
FROM SALES
WHERE Date LIKE '2023-01-%'
/* % shows all amount spent in JAN */
