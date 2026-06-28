# AWS E-Commerce Python Cloud Project

A complete end-to-end Data Analytics project that demonstrates how Python, SQL, and AWS cloud services can be used together to analyze an e-commerce dataset and generate business insights.

This project follows a real-world analytics workflow starting from data preprocessing in Python, relational database implementation using MySQL, cloud storage in AWS S3, SQL querying with AWS Athena, and interactive dashboard development using Streamlit.

---

# Project Overview

The objective of this project is to analyze the Brazilian E-Commerce Public Dataset by Olist and build a complete cloud-based analytics pipeline.

The project includes:

- Data preprocessing using Python
- Exploratory Data Analysis (EDA)
- Data cleaning and transformation
- Database creation using MySQL
- SQL analysis
- Cloud storage using AWS S3
- Cloud querying using AWS Athena
- Interactive dashboard using Streamlit
   
---

# Dataset

**Dataset Name**

Brazilian E-Commerce Public Dataset by Olist

Dataset contains:

- Customers
- Orders
- Order Items
- Products
- Sellers
- Payments
- Reviews
- Geolocation

Source:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

# Project Architecture

Dataset
↓

Python (Cleaning + EDA)
↓

MySQL Database

↓

AWS S3 Bucket

↓

AWS Athena Queries

↓

Streamlit Dashboard

<img width="900" height="500" alt="data analytics pipeline" src="https://github.com/user-attachments/assets/6250cd63-9938-46aa-827d-a68d2c8e5390" /> 

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Data Processing |
| Pandas | Data Cleaning |
| NumPy | Numerical Operations |
| Matplotlib | Visualization |
| Seaborn | Statistical Charts |
| MySQL | Database |
| SQL | Data Analysis |
| AWS S3 | Cloud Storage |
| AWS Athena | Cloud Query Engine |
| Streamlit | Dashboard |
| Git | Version Control |
| GitHub | Project Hosting |

---

# Project Folder Structure

```
AWS-E-Commerce-Python-Cloud-Project
│
├── Dataset
│
├── Python
│   ├── Data Cleaning
│   ├── EDA
│   └── KPI Analysis
│
├── SQL
│   └── Analysis Queries
│
├── Streamlit
│   └── Dashboard
│
├── Screenshots
│
├── README.md
│
└── requirements.txt
```

---

# Data Processing using Python

Python was used to import, clean, transform and analyze the datasets before storing them into the database.

### Activities Performed

- Imported CSV datasets using Pandas
- Examined dataset structure
- Handled missing values
- Removed duplicate records
- Converted data types
- Performed feature engineering
- Calculated KPIs
- Generated summary statistics

---

# Exploratory Data Analysis

Performed several exploratory analyses to understand customer behavior and business performance.

Analysis included:

- Order distribution
- Revenue analysis
- Product category analysis
- Payment analysis
- Customer analysis
- Seller analysis

---

# Database Implementation using MySQL

The cleaned datasets were imported into MySQL Workbench to create a relational database.

### Steps Performed

- Created Database
- Created Tables
- Imported CSV Files
- Defined Primary Keys
- Established Relationships
- Executed SQL Queries

---

# Sample SQL Queries

- Total Orders
- Total Revenue
- Average Order Value
- Top Selling Categories
- Monthly Sales
- Customer Distribution
- Payment Analysis
- Seller Performance

---

# Cloud Storage using AWS S3

The processed datasets were uploaded to Amazon S3 for scalable cloud storage.

### Activities

- Created S3 Bucket
- Uploaded CSV Files
- Verified Upload
- Managed Storage

<img width="700" height="200" alt="image" src="https://github.com/user-attachments/assets/4f45379b-c8d8-453b-a99a-8d0d40d39c5b" />

---

# Cloud Querying using AWS Athena

AWS Athena was used to execute SQL queries directly on files stored in Amazon S3 without loading them into a database.

### Activities

- Connected Athena with S3
- Created External Tables
- Executed SQL Queries
- Retrieved Results

 <img width="660" height="301" alt="image" src="https://github.com/user-attachments/assets/e903ebb1-d4db-4654-9bc3-fa9a2cea598e" />

---

# Dashboard using Streamlit

An interactive dashboard was created using Streamlit to visualize important business metrics.

Dashboard Features

- Total Orders
- Total Revenue
- Revenue Distribution
- Monthly Sales
- Order Status
- Product Categories
- Customer Insights
- Interactive Charts

---

# Key Performance Indicators

The dashboard provides important KPIs such as:

- Total Orders
- Total Revenue
- Average Order Value
- Payment Analysis
- Sales Distribution
- Product Performance

---

# Business Insights

Some insights generated from the analysis include:

- Revenue trends across orders
- Customer purchasing behavior
- Best-selling product categories
- Payment preferences
- Seller performance
- Order status distribution

---

# Skills Demonstrated

- Python Programming
- Data Cleaning
- Exploratory Data Analysis
- SQL
- Database Management
- AWS Cloud
- Amazon S3
- Amazon Athena
- Dashboard Development
- Streamlit
- Git
- GitHub

---

# Future Improvements

- Deploy Streamlit on AWS EC2
- Connect with Amazon RDS
- Automate ETL using AWS Glue
- Schedule data refresh
- Build Power BI Dashboard
- Add Machine Learning Prediction Model

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/yourusername/AWS-E-Commerce-Python-Cloud-Project.git
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run Streamlit

```bash
streamlit run app.py
```

---

# Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- MySQL
- AWS CLI
- Boto3

---

# Learning Outcomes

This project helped in understanding:

- End-to-end Data Analytics Workflow
- Cloud Data Storage
- SQL Analysis
- Data Visualization
- Dashboard Development
- Cloud Query Processing
- Version Control using Git

---
