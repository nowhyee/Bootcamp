/* Pull total number of orders that were completed on 18th March 2023 with the first name ‘John’ and last name Doe’ */
SELECT COUNT(DISTINCT Order_id) AS total_orders
FROM SALES
WHERE Date = '2023-03-18' ;

