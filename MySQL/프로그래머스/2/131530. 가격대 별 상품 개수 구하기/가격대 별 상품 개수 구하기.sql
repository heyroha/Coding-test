-- 코드를 입력하세요
WITH PRICE_TIER AS (
    SELECT PRODUCT_ID, FLOOR(PRICE/10000)* 10000 AS PRICE_GROUP
    FROM PRODUCT)

SELECT PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRICE_TIER
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP