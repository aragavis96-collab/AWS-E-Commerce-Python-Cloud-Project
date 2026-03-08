-----MYSQL WORKBENCH QUERIES


--REVENUE BY STATE
select c.customer_state,sum(oi.price) as revenue from orders o
join customers c on o.customer_id=c.customer_id
join order_items oi on o.order_id=oi.order_id
group by c.customer_state
order by revenue desc;

--TOP 10 SELLERS BY REVENUE
select seller_id, sum(price) as revenue from order_items
group by seller_id 
order by revenue desc
limit 10;

--REVENUE BY CATEGORY
select p.product_category_name, sum(oi.price) as revenue from order_items oi
join products p on oi.product_id=p.product_id
group by p.product_category_name
order by revenue desc;


--ORDER LEVEL ANALYSIS(YEAR,MONTH,STATUS)
select year(order_purchase_timestamp) as year, count(*) as total_orders from orders
group by year order by year;
select date_format(order_purchase_timestamp, '%Y-%m') as month, count(*) as total_orders from orders
group by month
order by month;
select order_status, count(*)*100.0/(select count(*) from orders) as percentage from orders
group by order_status;


--CUSTOMER BY STATE
select customer_state, count(*) as total_customers from customers
group by customer_state
order by total_customers desc;

--REVENUE PER CUSTOMER
select c.customer_unique_id, sum(oi.price) as revenue from orders o
join customers c on o.customer_id=c.customer_id
join order_items oi on o.order_id=oi.order_id
group by c.customer_unique_id
order by revenue desc;

--REPEAT CUSTOMER RATE
select count(*) as repeat_customers from(
  select customer_id from orders group by customer_id having count(order_id)  > 1
) as sub;

--SELLERS BY STATE
select seller_state, count(*) as total_sellers from sellers group by seller_state;

--SELLER REVENUE AND AVERAGE RATING
select s.seller_id, sum(oi.price) as revenue, avg(r.review_score) as avg_rating from order_items oi
join sellers s on oi.seller_id= s.seller_id
join orders o on oi.order_id = o.order_id
join order_reviews r on o.order_id = r.order_id
group by s.seller_id
order by revenue desc;

--TOP 10 PRODUCTS BY REVENUE
select product_id, sum(price) as revenue from order_items
group by product_id
order by revenue desc limit 10;

--REVENUE BY CATEGORY AND AVERAGE RATING
select p.product_category_name, sum(oi.price) as revenue, avg(r.review_score) as avg_rating from order_items oi
join products p on oi.product_id = p.product_id
join orders o on oi.order_id = o.order_id
join order_reviews r on o.order_id=r.order_id
group by p.product_category_name
order by revenue desc;

--REVENUE BY PAYMENT TYPE
select payment_type, sum(payment_value) as total_revenue, avg(payment_installments) as avg_installment from order_payment
group by payment_type
order by total_revenue desc;

--AVERAGE DELIVERY TIME BY STATE
select c.customer_state, avg(datediff(date(o.order_delivered_customer_date),date( o.order_purchase_timestamp)))  as avg_delivery_days from orders o
join customers c on o.customer_id =c.customer_id
where o.order_delivered_customer_date is not null
group by c.customer_state
order by avg_delivery_days desc;

--LATE DELIVERY PERCENTAGE BY SELLER
select s.seller_id, count(
                        case 
                              when o.order_delivered_customer_date > o.order_estimated_delivery_date
                              then 1 
						            end
					) *100.0/count(8) as  late_percentage from orders o
join order_items oi on o.order_id= oi.order_id
join sellers s on oi.seller_id = s.seller_id
where o.order_delivered_customer_date is not null
group by s.seller_id
order by late_percentage desc;

--REVENUE BY CUSTOMER CITY
select c.customer_city, sum(oi.price) as revenue from orders o
join customers c on o.customer_id = c.customer_id
join order_items oi on o.order_id = oi.order_id
group by c.customer_city
order by revenue desc;

--HOW MUCH REVENUE DOES TOP 20 SELLERS CONTRIBUTE
select sum(revenue) *100.0 / (select sum(price) from order_items) as top_20_percentage
  from (   
       select seller_id, sum(price) as revenue
       from order_items
       group by seller_id
       order by revenue desc
       limit 619
	) as top_sellers;
    
    
--STATE WISE REVENUE AND AVERAGE FREIGHT COST
select c.customer_state, sum(oi.price) as total_revenue, avg(oi.freight_value) as avg_freight from orders o
join customers c on o.customer_id=c.customer_id
join order_items oi on o.order_id=oi.order_id
group by c.customer_state
order by total_revenue desc;

--SELLER VS CUSTOMER STATE COMPARISON
select s.seller_state, c.customer_state, count(o.order_id) as total_orders, sum(oi.price) as revenue from orders o
join order_items oi on o.order_id=oi.order_id
join sellers s on oi.seller_id =s.seller_id
join customers c on o.customer_id =c.customer_id
group by s.seller_state, c.customer_state
order by revenue desc;

--AVERAGE PRODUCT SIZE BY CATEGORY
select pct.product_category_name_english, 
avg(p.product_weight_g) as avg_weight,
avg(p.product_length_cm) as avg_length,
avg(p.product_height_cm) as avg_height,
avg(p.product_width_cm) as avg_width from products p
join  product_category pct
on p.product_category_name=pct.product_category_name
group by pct.product_category_name_english
order by avg_weight desc;

--TOP 10 CUSTOMERS BY SPENDING
select c.customer_unique_id,round(sum(p.payment_value), 2) as total_spent from customers c
join orders o on c.customer_id = o.customer_id
join order_payment p on o.order_id = p.order_id
group by c.customer_unique_id
order by total_spent desc limit 10;

--HIGH FREIGHT BUT LOW PRODUCT VALUE(LOSS ANALYSIS)
select o.order_id, sum(oi.price) as total_price, sum(oi.freight_value) as total_freight from orders o
join order_items oi on o.order_id =oi.order_id
group by o.order_id
having total_freight > total_price
order by total_freight desc;

--REPEATE CUSTOMER RATE
select round(
        sum(case
               when order_count > 1 then 1 else 0 end) * 100.0 
        / count(*), 2
    ) as repeat_customer_rate
from (
    select 
        customer_unique_id,
        count(order_id) as order_count
    from  customers c
    join  orders o on c.customer_id = o.customer_id
    where o.order_status = 'delivered'
    group by customer_unique_id
) t;


--AVERAGE DELAY TIME IN DAYS
select round(avg(datediff(o.order_delivered_customer_date, o.order_purchase_timestamp)), 2) as avg_delivery_days
from orders o
where o.order_status = 'delivered';

--CATEGORY REVENUE CONTRIBUTION
select pct.product_category_name_english, sum(oi.price) as category_revenue,
   round(sum(oi.price)*100.0/ sum(sum(oi.price)) over(),2) as revenue_percentage from order_items oi
join products p on oi.product_id=p.product_id
join product_category pct on p.product_category_name = pct.product_category_name
group by pct.product_category_name_english
order by revenue_percentage desc;


--TOP PRODUCT CATEGORY PER MONTH
select *from (
    select date_format(o.order_purchase_timestamp, '%Y-%m') as order_month,pr.product_category_name,sum(oi.price) as total_sales,
        rank() over (
            partition by date_format(o.order_purchase_timestamp, '%Y-%m')
            order by sum(oi.price) desc
        ) as rnk
    from orders o
    join order_items oi on o.order_id = oi.order_id
    join products pr on oi.product_id = pr.product_id
    where o.order_status = 'delivered'
    group by order_month, pr.product_category_name
) ranked
where rnk = 1;
