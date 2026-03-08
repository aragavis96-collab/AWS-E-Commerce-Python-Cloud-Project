import streamlit as st
import pandas as pd
import plotly.express as px

orders = pd.read_csv("olist_orders_dataset.csv")
items = pd.read_csv("olist_order_items_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")

st.set_page_config(page_title="Olist Sales Dashboard", layout="wide")
st.title("Olist E-commerce Sales Dashboard")

orders = pd.read_csv("olist_orders_dataset.csv")
items = pd.read_csv("olist_order_items_dataset.csv")

total_orders = orders["order_id"].nunique()
total_revenue = items["price"].sum()

col1, col2 = st.columns(2)

col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"${total_revenue:,.2f}")

status = orders["order_status"].value_counts().reset_index()
status.columns = ["Status", "Count"]

fig1 = px.bar(
    status,
    x="Status",
    y="Count",
    color="Status",
    title="Orders by Status"
)

st.plotly_chart(fig1, use_container_width=True,key="chart1")

fig2 = px.histogram(
    items,
    x="price",
    nbins=50,
    title="Revenue Distribution",
    color_discrete_sequence=["purple"]
)

st.plotly_chart(fig2, use_container_width=True,key="chart2")


payments = pd.read_csv("olist_order_payments_dataset.csv")

payment = payments["payment_type"].value_counts().reset_index()
payment.columns = ["Payment Type", "Count"]

fig3 = px.pie(
    payment,
    values="Count",
    names="Payment Type",
    title="Payment Method Distribution"
)

st.plotly_chart(fig3, use_container_width=True,key="chart3")
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1)

with col2:
    st.plotly_chart(fig3)


fig1.update_layout(template="plotly_dark")
