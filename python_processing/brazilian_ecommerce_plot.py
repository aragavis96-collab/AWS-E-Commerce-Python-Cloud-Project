import matplotlib.pyplot as plt

#monthly order trend
monthly_orders=orders.groupby(['order_year','order_month']).size().reset_index(name='order_count')
plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_orders, x='order_month', y='order_count')
plt.title("Monthly Order Trend")
plt.show()

#order status distribution
plt.figure(figsize=(8,5))
sns.countplot(data=orders, x='order_status')
plt.xticks(rotation=90)
plt.title("Order Status Distribution")
plt.show()

#calculate delivery time
orders['delivery_time_days']=(
    orders['order_delivered_customer_date']-orders['order_purchase_timestamp']
).dt.days
plt.figure(figsize=(8,5))
sns.histplot(orders['delivery_time_days'], bins=30)
plt.title("Delivery Time Distribution (Days)")
plt.show()

#customer review
plt.figure(figsize=(8,5))
sns.countplot(data=order_review, x='review_score')
plt.title("Customer Review Distribution")
plt.show()

#monthly revenue
order_revenue=order_items.groupby('order_id')['price'].sum().reset_index()
orders_revenue=pd.merge(orders,order_revenue, on='order_id')
monthly_revenue=orders_revenue.groupby('order_month')['price'].sum().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(data=monthly_revenue, x='order_month',y='price')
plt.title("Monthly Revenue")
plt.show()

#customer segment
plt.figure(figsize=(8,5))
sns.countplot(data=rfm, x='Segment')
plt.xticks(rotation=90)
plt.title("Customer Segmentation")
plt.show()

#top sellers
seller_revenue=order_items.groupby('seller_id')['price'].sum().reset_index()
top_sellers= seller_revenue.sort_values(by='price', ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(data=top_sellers, x='seller_id', y='price')
plt.xticks(rotation=90)
plt.title("top 10 Sellers by Revenue")
plt.show()

#customer cohort retention
plt.figure(figsize=(12,6))
sns.heatmap(cohort_pivot,annot=False)
plt.title("Customer Cohort Retention")
plt.show()

#price distribution
plt.figure(figsize=(8,5))
sns.boxplot(x=order_items['price'])
plt.title("Price Distribution - Outlier Detection")
plt.show()

#revenue distribution
plt.figure(figsize=(8,5))
sns.histplot(order_items['price'],bins=50)
plt.title("Revenue Distribution")
plt.show()

#correlation matrix
numeric_cols=order_items.select_dtypes(include=np.number)
plt.figure(figsize=(8,6))
sns.heatmap(numeric_cols.corr(),annot=True, cmap='coolwarm',fmt=".2f",linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

#price vs freight value
plt.figure(figsize=(8,5))
sns.scatterplot(data=order_items, x='price', y='freight_value')
plt.title("Price vs Freight Value")
plt.xlabel("Product Price")
plt.ylabel("Freight Value")
plt.show()

#weight vs freight cost
product_merge = pd.merge(order_items, products, on='product_id')
plt.figure(figsize=(8,5))
sns.scatterplot(data=product_merge, x='product_weight_g',y='freight_value')
plt.title("Weight vs Freight Cost")
plt.xlabel("Product Weight (g)")
plt.ylabel("Freight Value")
plt.show()

#add regression line
plt.figure(figsize=(8,5))
sns.regplot(data=product_merge, x='product_weight_g', y='freight_value', scatter_kws={'alpha':0.3})
plt.title("Weight vs Freight (Regression)")
plt.show()

#delivery time vs customer review
orders['delivery_days']=(
    orders['order_delivered_customer_date']-orders['order_purchase_timestamp']
).dt.days
delivery_review=pd.merge(orders,order_review, on='order_id')
plt.figure(figsize=(8,5))
sns.stripplot(data=delivery_review, x='delivery_days', y='review_score')
plt.title("Delivey Time vs Customer Review")
plt.xlabel("Delivery Days")
plt.ylabel("Review Score")
plt.show()

#hexbin
plt.figure(figsize=(8,5))
plt.hexbin(product_merge['product_weight_g'],product_merge['freight_value'],gridsize=30)
plt.xlabel("Product Weight")
plt.ylabel("Freight Value")
plt.title("Hexbin: Weight vs Freight")
plt.colorbar()
plt.show()

#delivery time density distribution
plt.figure(figsize=(8,5))
sns.kdeplot(data=orders, x='delivery_days', fill=True)
plt.title("Delivery Time Density Distribution")
plt.xlabel("Delivery days")
plt.show()

#seller revenue vs ratings
seller_data=pd.merge(order_items, order_review,  on ='order_id')
seller_summary= seller_data.groupby('seller_id').agg({
    'price':'sum',
    'review_score':'mean'
}).reset_index()
plt.figure(figsize=(8,5))
sns.violinplot(data=seller_summary, x='price',y='review_score')
plt.title("Seller Revenue vs Rating")
plt.xlabel("Total Revenue")
plt.ylabel("Average Rating")
plt.show()
