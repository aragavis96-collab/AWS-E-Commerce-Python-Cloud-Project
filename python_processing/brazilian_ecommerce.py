#customer city
customers['customer_city_clean']=customers['customer_city'].apply(
    lambda x: ''.join(char for char in str(x) if ord(char)<128)
)
customers[['customer_city','customer_city_clean']].head()

#clean customer_city
customers['customer_city_clean']=(customers['customer_city_clean'].str.lower().str.strip())
customers['customer_city_clean'].head()

#find rows special characters
def has_non_ascii(text):
    return any(ord(char) >127 for char in str(text))
special_rows=customers[customers['customer_city'].apply(has_non_ascii)]
special_rows.head()

#filter cities starting with vowels
vowels=[ord('A'),ord('E'),ord('I'),ord('O'),ord('U'),ord('a'),ord('e'),ord('i'),ord('o'),ord('u')]
vowel_cities=customers[customers['customer_city'].apply(lambda x: ord(str(x)[0]) in vowels)]
vowel_cities.head()

#convert first letter to ascii number
customers['city_first_letter_ascii']=customers['customer_city'].apply(
    lambda x :ord(str(x)[0])
)
customers[['customer_city','city_first_letter_ascii']].head()

#convert ascii back to character
customers['ascii_back_to_char']=customers['city_first_letter_ascii'].apply(chr)
customers[['city_first_letter_ascii','ascii_back_to_char']].head()

#sort cities based on ascii
customers_sorted=customers.sort_values(by='city_first_letter_ascii')
customers_sorted.head()

#number of cities with special characters
non_ascii_count=customers['customer_city'].apply(
    lambda x: any(ord(char) >127 for char in str(x))
).sum()
print("Number of cities with special characters:",non_ascii_count)

#convert datetime
orders['order_purchase_timestamp']=pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_approved_at']=pd.to_datetime(orders['order_approved_at'])
orders['order_delivered_carrier_date']=pd.to_datetime(orders['order_delivered_carrier_date'])
orders['order_delivered_customer_date']=pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_estimated_delivery_date']=pd.to_datetime(orders['order_estimated_delivery_date'])
orders.info()
order_review['review_creation_date']=pd.to_datetime(order_review['review_creation_date'])
order_review['review_answer_timestamp']=pd.to_datetime(order_review['review_answer_timestamp'])
order_review.info()
order_items['shipping_limit_date']=pd.to_datetime(order_items['shipping_limit_date'])
order_items.info()

orders['order_purchase_timestamp']=pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_year']=orders['order_purchase_timestamp'].dt.year
orders['order_month']=orders['order_purchase_timestamp'].dt.month
orders['order_day']=orders['order_purchase_timestamp'].dt.day
orders['order_dayofweek']=orders['order_purchase_timestamp'].dt.day_name()
orders[['order_year','order_month','order_day','order_dayofweek']].head()

#late delivery
orders['is_late']=orders['order_delivered_customer_date'] > orders['order_estimated_delivery_date']
late_percentage= orders['is_late'].mean()*100
print("Late Delivery %:",round(late_percentage,2))

#merge revenue
order_revenue=order_items.groupby('order_id')['price'].sum().reset_index()
orders_rfm=pd.merge(orders,order_revenue, on='order_id')
orders_rfm=orders_rfm[orders_rfm['order_status']=='delivered']
orders_rfm.info()
orders_rfm.shape
orders_rfm['order_status'].value_counts()

#create RFM Table
snapshot_date=orders_rfm['order_purchase_timestamp'].max()
rfm=orders_rfm.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x:(snapshot_date - x.max()).days ,
    'order_id': 'count',
    'price': 'sum'
}).reset_index()
rfm.columns=['customer_id','Recency','Frequency','Monetary']
rfm.head()

#RFM score
rfm['R_score']=pd.qcut(rfm['Recency'],4, labels=[4,3,2,1])
rfm['F_score']=pd.qcut(rfm['Frequency'].rank(method='first'),4 ,labels=[1,2,3,4])
rfm['M_score']=pd.qcut(rfm['Monetary'], 4, labels=[1,2,3,4])
rfm['RFM_score']=rfm[['R_score','F_score','M_score']].astype(str).sum(axis=1)
rfm['RFM_score']=rfm[['R_score','F_score',"M_score"]].astype(int).sum(axis=1)
rfm.head()

#segment customers
def segment(row):
    if row['RFM_score']=='444':
        return 'Champions'
    elif row['F_score']==4:
        return 'Loyal Customers'
    elif row['R_score']==4:
        return 'Recent Customers'
    else:
        return 'Others'
rfm['Segment']=rfm.apply(segment, axis=1)
rfm.head()

#seller review
seller_reviews=pd.merge(order_items,order_review,on='order_id')
seller_rating = seller_reviews.groupby('seller_id')['review_score'].mean().reset_index()
seller_rating.head()

#cohort analysis
orders=orders.copy()
orders['order_purchase_timestamp']=pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_month']=orders['order_purchase_timestamp'].dt.to_period('M')
cohort=(
    orders
    .groupby('customer_id')['order_month']
    .min()
    .reset_index()
    .rename(columns={'order_month': 'cohort_month'})
)
cohort.columns=['customer_id','cohort_month']

#remove old column if exists
orders=orders.drop(columns=['cohort_month'],errors='ignore')

#merging columns
orders=orders.merge(cohort, on='customer_id',how='left')
orders.head()

#cohort shape
cohort_data=orders.groupby(['cohort_month','order_month'])\
            .agg(n_customers=('customer_id','nunique'))\
            .reset_index()
cohort_pivot=cohort_data.pivot(index='cohort_month',
                              columns='order_month',
                              values='n_customers')
cohort_pivot.shape

#total values
total_revenue=order_items['price'].sum()
total_orders=orders['order_id'].nunique()
total_customers=orders['customer_id'].nunique()
avg_order_value=total_revenue/total_orders
print("Total Revenue:",round(total_revenue,2))
print("Total Orders:",total_orders)
print("Total Customers:",total_customers)
print("Average Order Value:",round(avg_order_value,2))

#missing value audit
def missing_report(df):
    missing =df.isnull().sum()
    percent = (missing/len(df))*100
    report =pd.DataFrame({
        'Missing_Count':missing,
        'Missing_Percentage':percent
    })
    return report[report['Missing_Count']>0].sort_values(by='Missing_Percentage', ascending=False)
missing_report(orders)
missing_report(order_review)
missing_report(products)

#number of outliers
Q1=order_items['price'].quantile(0.25)
Q3=order_items['price'].quantile(0.75)
IQR= Q3-Q1
upper=Q3+1.5*IQR
lower=Q1-1.5*IQR
outliers=order_items[(order_items['price'] < lower)|(order_items['price'] > upper)]
print("Number of Outliers:", len(outliers))

#executive summary
print("=== EXECUTIVE SUMMARY ===")
print("Total Orders:", orders['order_id'].nunique())
print("Total Revenue:", round(order_items['price'].sum(),2))
print("Average Delivery Time:", round(orders['delivery_time_days'].mean(),2))
print("Late Delivery %:", round(orders['is_late'].mean()*100,2))
