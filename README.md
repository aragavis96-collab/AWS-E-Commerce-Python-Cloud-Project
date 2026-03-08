# AWS-E-Commerce-Python-Cloud-Project
This project showcases a comprehensive data analytics workflow that utilizes Python and cloud technologies to examine an e-commerce dataset and produce insights. It involves data processing, database management, cloud-based querying, and dashboard visualization, emulating a basic data engineering pipeline.

# Dataset discription
The study makes use of the Brazilian E-Commerce Public Dataset from Olist, which consists of many CSV files that illustrate multiple facets of an e-commerce website.
Dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce.
Orders, customers, product details, payments, reviews, and sellers information are all included in these datasets.

# Project Overflow Diagram
This figure shows the steps from dataset input to data processing in Python, SQL analysis, cloud storage in AWS S3, querying using AWS Athena, and visualization using Streamlit.
<img width="900" height="500" alt="data analytics pipeline" src="https://github.com/user-attachments/assets/6250cd63-9938-46aa-827d-a68d2c8e5390" />

# 📊 Data processing using python
Python was used to import the dataset into a Jupyter Notebook for preliminary data exploration and analysis. This stage aided in comprehending the data's structure and getting it ready for additional processing and display.

Activities carried out:
-------
📌Using Pandas to import datasets

📌Examining the structure of datasets

📌Carrying out simple data cleansing

📌Performing fundamental statistical analysis

📌Finding important KPIs like revenue and total orders

# 🗄️ Database implementation using MYSQL
The datasets were imported into MySQL Workbench to establish a relational database environment following preliminary data analysis in Jupyter Notebook. This stage made it possible to store structured data and run SQL queries for further comprehensive examination.

Steps Performed
-------
📌Creating a database
         
📌CSV file importation into database tables

📌Running queries in SQL for analysis

Executed Example Queries
---------
👉 Calculating the total quantity of orders

👉 Finding the overall revenue

👉 Connecting several tables to do out relationship analysis

# ☁️ Cloud Storage Using AWS S3
The project data was stored in a scalable secured cloud storage environment by uploading the CSV datasets to an Amazon S3 bucket. This facilitates the data's easy access and processing for additional analysis by various other cloud-based services.

Steps performed:
---------
📂 Creating an S3 bucket

📤 Uploading dataset files

✅ Verifying uploaded data

<img width="700" height="200" alt="image" src="https://github.com/user-attachments/assets/4f45379b-c8d8-453b-a99a-8d0d40d39c5b" />

# 🔎 Cloud Querying using AWS Athena 
SQL queries were run directly on the datasets kept in the S3 bucket using Amazon Athena. This eliminated the requirement for a conventional database configuration and enabled effective querying and analysis of massive datasets.

Steps performed:
-----
📌Connecting Athena with S3

📌Creating external Tables referencing s3 data

📌Executing SQL Queries

Example Queries:
-------
👉 Order status distribution

👉 Product Category Review Score 

<img width="660" height="301" alt="image" src="https://github.com/user-attachments/assets/e903ebb1-d4db-4654-9bc3-fa9a2cea598e" />

# 📈Data Visualization using Streamlit
Streamlit was used to create a live dashboard that showed the primary results from the dataset. Streamlit assists in transforming data research findings into easily understood and interactive visual elements like graphs, charts, and metrics. This makes it simple for consumers to understand the important details and examine the data in an understandable and practical manner.

Dashboard features include:
------
📌Total Orders metric

Displays the total number of orders in the dataset, providing an overview of the overall transaction volume.

<img width="400" height="175" alt="image" src="https://github.com/user-attachments/assets/29236fd4-5ce2-4661-8d87-55d5330f15c8" />



📌Total Revenue metric

Displays the total revenue made by all orders, enabling someone to more effectively assess the entire business performance.

<img width="676" height="150" alt="revenue" src="https://github.com/user-attachments/assets/9462a835-b942-4e39-b3d0-1a8ca2964e0f" />



📌Orders by Status chart

Visualizes the distribution of orders corresponding their current status, such as delivered, shipped, cancelled or so on.

<img width="889" height="347" alt="image" src="https://github.com/user-attachments/assets/93dbdab5-bc88-45a4-b210-b5c211a4d976" />

