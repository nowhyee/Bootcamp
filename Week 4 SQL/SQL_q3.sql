/* Pull the departments that generated less than $600 in 2022 */
SELECT Department
FROM ITEMS
WHERE Department IN (
  SELECT I.Department
  FROM SALES S
  JOIN ITEMS I ON S.Item_id = I.Item_id
  WHERE S.Date LIKE '2022-%'
  GROUP BY I.Department
  HAVING SUM(S.Revenue) < 600
  ) ;
