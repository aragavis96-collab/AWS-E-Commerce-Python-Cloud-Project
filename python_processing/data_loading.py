# This code was executed in Kaggle environment
# Dataset path refers to Kaggle input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

/*----------------------------------importing dataset as csv-------------------------------*/
customers=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_customers_dataset.csv'))
sellers=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_sellers_dataset.csv'))
order_review=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_order_reviews_dataset.csv'))
order_items=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_order_items_dataset.csv'))
products=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_products_dataset.csv'))
g_location=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_geolocation_dataset.csv'))
p_category=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/product_category_name_translation.csv'))
orders=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_orders_dataset.csv'))
o_payment=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_order_payments_dataset.csv'))

/*--------------------------------------------printing tables-----------------------------*/
order_items.head()
order_review.head()
sellers.head()
customers.head()
o_payment.head()
products.head()
g_location.head()
p_category.head()
orders.head()
