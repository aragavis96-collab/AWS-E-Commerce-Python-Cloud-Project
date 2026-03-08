# This code was executed in Kaggle environment
# Dataset path refers to Kaggle input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


customers=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_customers_dataset.csv'))
customers.head()
customers.isnull().sum()
customers.shape
customers.info()
customers.duplicated().sum()

sellers=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_sellers_dataset.csv'))
sellers.head()
sellers.isnull().sum()
sellers.shape
sellers.info()
sellers.duplicated().sum()

order_review=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_order_reviews_dataset.csv'))
order_review.head()
order_review.isnull().sum()
order_review.shape
order_review.info()
order_review.duplicated().sum()

order_items=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_order_items_dataset.csv'))
order_items.head()
order_items.isnull().sum()
order_items.shape
order_items.info()
order_items.duplicated().sum()

products=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_products_dataset.csv'))
products.head()
products.isnull().sum()
products.shape
products.info()
products.duplicated().sum()

g_location=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_geolocation_dataset.csv'))
.head()
g_location.isnull().sum()
g_location.shape
g_location.info()
g_location.duplicated().sum()

p_category=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/product_category_name_translation.csv'))
p_category.head()
p_category.isnull().sum()
p_category.shape
p_category.info()
p_category.duplicated().sum()

orders=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_orders_dataset.csv'))
orders.head()
orders.isnull().sum()
orders.shape
orders.info()
orders.duplicated().sum()

o_payment=pd.read_csv(os.path.join('/kaggle/input/datasets/organizations/olistbr/brazilian-ecommerce/olist_order_payments_dataset.csv'))
o_payment.head()
o_payment.isnull().sum()
o_payment.shape
o_payment.info()
o_payment.duplicated().sum()


