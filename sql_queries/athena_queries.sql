---------AMAZON WEB SERVICE (AWS) ATHENA QUERIES


--TOTAL ORDERS AND REVENUE
SELECT count(distinct o.order_id) as total_orders, sum(oi.price + oi.freight_value) as total_revenue
from orders o
join order_items oi on o.order_id = oi.order_id;

--MONTHLY SALES TREND
SELECT DATE_TRUNC('month',cast(ORDER_PURCHASE_TIMESTAMP AS timestamp)) as month, COUNT(ORDER_ID) AS TOTAL_ORDERS
FROM ORDERS
GROUP BY date_trunc('month',cast(order_purchase_timestamp as timestamp))
ORDER BY MONTH;

--TOP 10 PRODUCT CATEGORIES
SELECT P.PRODUCT_CATEGORY_NAME, COUNT(*) AS TOTAL_ORDERS
FROM ORDER_ITEMS OI
JOIN PRODUCTS P ON OI.PRODUCT_ID = P.PRODUCT_ID
GROUP BY P.PRODUCT_CATEGORY_NAME
ORDER BY TOTAL_ORDERS desc
LIMIT 10;

--PAYMENT TYPE DISTRIBUTION
SELECT PAYMENT_TYPE, COUNT(*) AS TOTAL_PAYMENTS
FROM order_payments
GROUP BY PAYMENT_TYPE
ORDER BY TOTAL_PAYMENTS DESC;

--AVERAGE DELIVERY TIME
SELECT AVG(DATE_DIFF('day', try_cast(ORDER_PURCHASE_TIMESTAMP as timestamp),try_cast(ORDER_DELIVERED_CUSTOMER_DATE as timestamp)))
AS AVG_DELIVERY_DAYS
FROM ORDERS
WHERE ORDER_DELIVERED_CUSTOMER_DATE IS NOT NULL;

--TOP CITITES BY CUSTOMERS
SELECT g.geolocation_city, COUNT(DISTINCT c.customer_unique_id) AS total_customers
FROM customers c
JOIN GEOLOCATION G ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
GROUP BY G.GEOLOCATION_CITY
ORDER BY TOTAL_CUSTOMERS DESC
LIMIT 10;

--TOP PRODUCT PER CATEGORY
SELECT * from(
       SELECT pct.product_category_name_english as category, oi.product_id, count(*) as total_orders, 
       RANK() OVER (PARTITION BY pct.product_category_name_english 
       order by count(*) desc) as rank_in_category
       from order_items oi
       join products p on oi.product_id = p.product_id
       join product_category pct on p.product_category_name = pct.product_category_name
       group by pct.product_category_name_english, oi.product_id
    )t
where rank_in_category =1;


--SELLER VS CUSTOMER STATE
SELECT s.seller_state, c.customer_state, count(*) as total_orders 
from order_items oi 
join sellers s on oi.seller_id = s.seller_id
join orders o on oi.order_id = o.order_id
join customers c on o.customer_id = c.customer_id
group by s.seller_state, c.customer_state
order by total_orders desc;

--AVERAGE REVIEW SCORE PER PRODUCT CATEGORY
SELECT p.product_category_name, avg(r.review_score) as avg_review_score
from order_reviews r
join orders o on r.order_id = o.order_id 
join order_items oi on o.order_id = oi.order_id 
join products p on oi.product_id = p.product_id
group by p.product_category_name
order by avg_review_score desc;
