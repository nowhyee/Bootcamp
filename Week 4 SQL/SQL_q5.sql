/* What were the orders that were purchased in our most lucrative order */

SELECT Order_id, Item_id, Quantity, Revenue
FROM SALES
WHERE Order_id = (
  SELECT Order_id
  FROM (
  SELECT Order_id, SUM(Revenue) AS order_revenue
  FROM SALES
  GROUP BY Order_id
  ORDER BY order_revenue DESC
  LIMIT 1
  ) AS top_order
) ;
