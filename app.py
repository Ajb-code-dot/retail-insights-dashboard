import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Retail Insights Dashboard", page_icon="🛍️", layout="wide")

# Title
st.title("🛍️ Retail Insights Dashboard")
st.markdown("### Created by **Ajal Biju**")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your sales data (CSV file)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show preview
    st.subheader("📊 Preview of Uploaded Data")
    st.dataframe(df.head())

    # Show stats
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    # Sales by Category
    if "Category" in df.columns and "Sales" in df.columns:
        st.subheader("🛒 Sales by Category")
        category_sales = df.groupby("Category")["Sales"].sum()
        st.bar_chart(category_sales)

    # Monthly Sales Trend
    if "Date" in df.columns and "Sales" in df.columns:
        st.subheader("📅 Monthly Sales Trend")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Month"] = df["Date"].dt.to_period("M")
        monthly_sales = df.groupby("Month")["Sales"].sum()
        st.line_chart(monthly_sales)

    # Top Products
    if "Product" in df.columns and "Sales" in df.columns:
        st.subheader("🏆 Top 5 Products")
        top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)
        st.bar_chart(top_products)

    # Footer
    st.markdown("---")
    st.markdown("🚀 Built with [Streamlit](https://streamlit.io/) | 👨‍💻 Author: **Ajal Biju**")

else:
    st.info("⬆️ Please upload a CSV file to start the analysis.")

