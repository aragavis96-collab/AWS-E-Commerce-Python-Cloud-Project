import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.main{
background:#F5F7FA;
}

.block-container{
padding-top:0.3rem;
padding-left:1rem;
padding-right:1rem;
padding-bottom:0.3rem;
}

[data-testid="stMetric"]{
background:white;
padding:10px;
border-radius:12px;
box-shadow:0px 2px 8px rgba(0,0,0,0.08);
border-left:5px solid #1E3A8A;
}

background:white;

padding:15px;

border-radius:15px;

box-shadow:0px 3px 12px rgba(0,0,0,0.12);

text-align:center;

}

h1{
color:#1E3A8A;
font-weight:700;
}

div[data-testid="stPlotlyChart"]{
    background:white;
    padding:8px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
}
section[data-testid="stSidebar"]{
    width:230px !important;
}           
</style>
""",unsafe_allow_html=True)

st.markdown(
    "<h2 style='margin-bottom:5px;color:#1E3A8A;'>🛒 Olist Executive Dashboard</h2>",
    unsafe_allow_html=True
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "archive"

@st.cache_data
def load_data():

    customers = pd.read_csv(DATA_DIR/"olist_customers_dataset.csv")

    orders = pd.read_csv(DATA_DIR/"olist_orders_dataset.csv")

    payments = pd.read_csv(DATA_DIR/"olist_order_payments_dataset.csv")

    items = pd.read_csv(DATA_DIR/"olist_order_items_dataset.csv")

    products = pd.read_csv(DATA_DIR/"olist_products_dataset.csv")

    reviews = pd.read_csv(DATA_DIR/"olist_order_reviews_dataset.csv")

    sellers = pd.read_csv(DATA_DIR/"olist_sellers_dataset.csv")

    category = pd.read_csv(DATA_DIR/"product_category_name_translation.csv")

    return (
        customers,
        orders,
        payments,
        items,
        products,
        reviews,
        sellers,
        category
    )
(
customers,
orders,
payments,
items,
products,
reviews,
sellers,
category
)=load_data()
orders["order_purchase_timestamp"]=pd.to_datetime(
orders["order_purchase_timestamp"]
)
orders["Year"]=orders[
"order_purchase_timestamp"
].dt.year
orders["Month"]=orders[
"order_purchase_timestamp"
].dt.strftime("%b")

dashboard_df = (
orders

.merge(customers,on="customer_id")

.merge(payments,on="order_id")

.merge(items,on="order_id")

.merge(sellers, on="seller_id")

.merge(products,on="product_id")

.merge(
category,
on="product_category_name",
how="left"
)
)

# SIDEBAR FILTERS
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3081/3081559.png",
    width=80
)

st.sidebar.title("Dashboard Filters")

# YEAR FILTER
years = sorted(
    dashboard_df["Year"].dropna().unique()
)
selected_year = st.sidebar.multiselect(
    "Select Year",
    options=years,
    default=years
)

# STATE FILTER
states = sorted(
    dashboard_df["customer_state"].dropna().unique()
)
selected_state = st.sidebar.multiselect(
    "Customer State",
    options=states,
    default=states
)

# PAYMENT FILTER
payment_types = sorted(
    dashboard_df["payment_type"].dropna().unique()
)
selected_payment = st.sidebar.multiselect(
    "Payment Type",
    options=payment_types,
    default=payment_types
)

# FILTER DATA
filtered_df = dashboard_df[
    (dashboard_df["Year"].isin(selected_year))
    &
    (dashboard_df["customer_state"].isin(selected_state))
    &
    (dashboard_df["payment_type"].isin(selected_payment))
]

# KPI CALCULATIONS
total_revenue = filtered_df["payment_value"].sum()
total_orders = filtered_df["order_id"].nunique()
total_customers = filtered_df["customer_unique_id"].nunique()
total_products = filtered_df["product_id"].nunique()
total_sellers = filtered_df["seller_id"].nunique()
average_order = filtered_df["payment_value"].mean()

# KPI CARDS
st.markdown("## Executive Overview")
kpi1, kpi2, kpi3, kpi4= st.columns(4)
with kpi1:
    st.metric(
        "💰 Revenue",
        f"R$ {total_revenue:,.0f}"
    )
with kpi2:
    st.metric(
        "📦 Orders",
        f"{total_orders:,}"
    )
with kpi3:
    st.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )
with kpi4:
    st.metric(
        "🏪 Sellers",
        f"{total_sellers:,}"
    )

st.markdown("---")

# ROW 1
# Revenue Trend & Payment Method
left_col, right_col = st.columns([2, 1])

# Monthly Revenue Trend
with left_col:
    st.subheader("📈 Monthly Revenue Trend")
    monthly_sales = (
        filtered_df
        .groupby("Month", sort=False)["payment_value"]
        .sum()
        .reset_index()
    )
    month_order = [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]
    monthly_sales["Month"] = pd.Categorical(
        monthly_sales["Month"],
        categories=month_order,
        ordered=True
    )
    monthly_sales = monthly_sales.sort_values("Month")
    fig_line = px.line(
        monthly_sales,
        x="Month",
        y="payment_value",
        markers=True
    )
    fig_line.update_layout(
        template="simple_white",
        height=380,
        margin=dict(l=10,r=10,t=30,b=10),
        xaxis_title="",
        yaxis_title="Revenue (R$)"
    )
    fig_line.update_traces(
        line_width=4
    )
    st.plotly_chart(
        fig_line,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# Payment Method
with right_col:
    st.subheader("💳 Payment Methods")
    payment_chart = (
        filtered_df
        .groupby("payment_type")["payment_value"]
        .sum()
        .reset_index()
    )
    fig_pie = px.pie(
        payment_chart,
        names="payment_type",
        values="payment_value",
        hole=0.65
    )
    fig_pie.update_layout(
        template="plotly_white",
        height=200,
        margin=dict(l=10,r=10,t=30,b=10),
        showlegend=True
    )
    fig_pie.update_traces(
        textposition="inside",
        textinfo="percent"
    )
    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

# ROW 2
# Top Categories & Order Status
left_col, right_col = st.columns([2, 1])

# Top Product Categories
with left_col:
    st.subheader("📦 Top 10 Product Categories")
    category_sales = (
        filtered_df
        .groupby("product_category_name_english")
        .agg(
            Orders=("order_id", "nunique")
        )
        .reset_index()
    )
    category_sales = (
        category_sales
        .sort_values(
            by="Orders",
            ascending=False
        )
        .head(10)
    )
    fig_category = px.bar(
        category_sales,
        x="Orders",
        y="product_category_name_english",
        orientation="h",
        text="Orders"
    )
    fig_category.update_layout(
        template="plotly_white",
        height=200,
        margin=dict(l=10,r=10,t=30,b=10),
        yaxis_title="",
        xaxis_title="Orders"
    )
    fig_category.update_traces(
        textposition="outside"
    )
    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

# Order Status
with right_col:
    st.subheader("🚚 Order Status")
    status_df = (
        filtered_df["order_status"]
        .value_counts()
        .reset_index()
    )
    status_df.columns = [
        "Status",
        "Orders"
    ]
    fig_status = px.bar(
        status_df,
        x="Status",
        y="Orders",
        text="Orders"
    )
    fig_status.update_layout(
        template="plotly_white",
        height=200,
        margin=dict(l=10,r=10,t=30,b=10),
        xaxis_title="",
        yaxis_title="Orders"
    )
    st.plotly_chart(
        fig_status,
        use_container_width=True
    )

# ROW 3
# Customer States & Seller States
left_col, right_col = st.columns(2)

# Customer States
with left_col:
    st.subheader("🌍 Top Customer States")
    customer_state_df = (
        filtered_df
        .groupby("customer_state")
        .agg(Customers=("customer_unique_id","nunique"))
        .reset_index()
        .sort_values("Customers", ascending=False)
        .head(10)
    )
    fig_customer = px.bar(
        customer_state_df,
        x="customer_state",
        y="Customers",
        text="Customers"
    )
    fig_customer.update_layout(
        template="plotly_white",
        height=180,
        margin=dict(l=10,r=10,t=30,b=10),
        xaxis_title="State",
        yaxis_title="Customers"
    )
    st.plotly_chart(
        fig_customer,
        use_container_width=True
    )

# Seller States

with right_col:
    st.subheader("🏪 Top Seller States")
    seller_state_df = (
        filtered_df
        .groupby("seller_state")
        
        .agg(Sellers=("seller_id","nunique"))
        .reset_index()
        .sort_values("Sellers", ascending=False)
        .head(10)
    )
    fig_seller = px.bar(
        seller_state_df,
        x="seller_state",
        y="Sellers",
        text="Sellers"
    )
    fig_seller.update_layout(
        template="plotly_white",
        height=180,
        margin=dict(l=10,r=10,t=30,b=10),
        xaxis_title="State",
        yaxis_title="Sellers"
    )
    st.plotly_chart(
        fig_seller,
        use_container_width=True
    )

# REVIEW ANALYSIS
st.markdown("---")
st.subheader("⭐ Customer Review Distribution")
review_chart = (
    reviews["review_score"]
    .value_counts()
    .sort_index()
    .reset_index()
)
review_chart.columns = [
    "Rating",
    "Reviews"
]
fig_review = px.bar(
    review_chart,
    x="Rating",
    y="Reviews",
    text="Reviews"
)
fig_review.update_layout(
    template="plotly_white",
    height=180,
    margin=dict(l=10,r=10,t=30,b=10),
    xaxis_title="Review Score",
    yaxis_title="Reviews"
)
st.plotly_chart(
    fig_review,
    use_container_width=True
)

# SIDEBAR SUMMARY
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Summary")
st.sidebar.metric(
    "Orders",
    f"{filtered_df['order_id'].nunique():,}"
)
st.sidebar.metric(
    "Revenue",
    f"R$ {filtered_df['payment_value'].sum():,.0f}"
)
st.sidebar.metric(
    "Customers",
    f"{filtered_df['customer_unique_id'].nunique():,}"
)
st.sidebar.metric(
    "Sellers",
    f"{filtered_df['seller_id'].nunique():,}"
)

# DOWNLOAD FILTERED DATA
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.sidebar.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="filtered_dashboard_data.csv",
    mime="text/csv"
)

# DATA PREVIEW
with st.expander("📋 View Filtered Dataset",expanded=False):
    st.dataframe(
        filtered_df.head(100),
        use_container_width=True
    )

# FOOTER
st.markdown("---")
st.markdown(
"""
<div style='text-align:center'>
##### 🛒 Olist E-Commerce Dashboard
</div>
""",
unsafe_allow_html=True
)
