import streamlit as st
import pandas as pd
import joblib

# Load pipeline
st.markdown("""
    <style>
    .main {background-color: #f5f7fa;}
    </style>
    """, unsafe_allow_html=True)
model = joblib.load('sales_pipeline.pkl')

st.set_page_config(page_title="Sales Forecasting App", layout="wide")

st.title("📊 Smart Sales Forecasting System")
st.write("Predict product sales using Machine Learning")

# Sidebar

st.sidebar.header("Enter Product Details")

item_weight = st.sidebar.number_input("Item Weight", 0.0)
item_visibility = st.sidebar.number_input("Item Visibility", 0.0)
item_mrp = st.sidebar.number_input("Item MRP", 0.0)
outlet_age = st.sidebar.number_input("Outlet Age", 0)

fat = st.sidebar.selectbox("Fat Content", ["Low Fat", "Regular"])
item_type = st.sidebar.selectbox("Item Type", [
"Dairy", "Soft Drinks", "Meat", "Fruits and Vegetables",
"Household", "Baking Goods", "Snack Foods", "Frozen Foods"
])

outlet_size = st.sidebar.selectbox("Outlet Size", ["Small", "Medium", "High"])
location = st.sidebar.selectbox("Outlet Location", ["Tier 1", "Tier 2", "Tier 3"])
outlet_type = st.sidebar.selectbox("Outlet Type", [
"Grocery Store", "Supermarket Type1", "Supermarket Type2"
])

category = st.sidebar.selectbox("Item Category", ["Food", "Drinks", "Non-Consumable"])

# Create input dataframe (RAW format only)

input_data = pd.DataFrame({
'Item_Weight': [item_weight],
'Item_Visibility': [item_visibility],
'Item_MRP': [item_mrp],
'Outlet_Age': [outlet_age],
'Item_Fat_Content': [fat],
'Item_Type': [item_type],
'Outlet_Size': [outlet_size],
'Outlet_Location_Type': [location],
'Outlet_Type': [outlet_type],
'Item_Category': [category]
})

# Predict

if st.button("Predict Sales"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Sales: {prediction[0]:,.2f}")


# import streamlit as st
# import pandas as pd
# import joblib

# # Load model and columns

# model = joblib.load('model.pkl')
# columns = joblib.load('columns.pkl')

# # Page config

# st.set_page_config(page_title="Sales Forecasting App", layout="wide")

# st.title("📊 Sales Forecasting System")
# st.write("Enter product details to predict sales")

# # Sidebar inputs

# st.sidebar.header("Input Features")

# data = {}

# for col in columns:
#     data[col] = st.sidebar.number_input(col, value=0.0)

# # Convert to DataFrame

# input_df = pd.DataFrame([data])

# # Prediction

# if st.button("Predict Sales"):
#     prediction = model.predict(input_df)
#     st.success(f"Estimated Sales: {prediction[0]:.2f}")


# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Load model

# model = joblib.load('sales_model.pkl')

# st.set_page_config(page_title="Sales Forecasting App", layout="wide")

# st.title("📊 Sales Forecasting System")
# st.write("Predict product sales using Machine Learning")

# # Sidebar Inputs

# st.sidebar.header("Input Product Details")

# Item_Weight = st.sidebar.number_input("Item Weight", min_value=0.0)
# Item_Visibility = st.sidebar.number_input("Item Visibility", min_value=0.0)
# Item_MRP = st.sidebar.number_input("Item MRP", min_value=0.0)
# Outlet_Age = st.sidebar.number_input("Outlet Age", min_value=0)

# # Simple categorical example

# Item_Fat_Content = st.sidebar.selectbox("Fat Content", ["Low Fat", "Regular"])

# # Convert manually (same encoding used earlier)

# fat_map = {"Low Fat": 0, "Regular": 1}
# Item_Fat_Content = fat_map[Item_Fat_Content]

# # Create input dataframe

# input_data = pd.DataFrame({
# 'Item_Weight': [Item_Weight],
# 'Item_Visibility': [Item_Visibility],
# 'Item_MRP': [Item_MRP],
# 'Outlet_Age': [Outlet_Age],
# 'Item_Fat_Content': [Item_Fat_Content]
# })

# # Prediction

# if st.button("Predict Sales"):
#     prediction = model.predict(input_data)
#     st.success(f"Estimated Sales: {prediction[0]:.2f}")
