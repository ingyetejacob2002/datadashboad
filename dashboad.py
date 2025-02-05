import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Interactive Dashboard",
    page_icon="📊",
    layout="wide",
)

# Sidebar
st.sidebar.title("Dashboard Settings")
st.sidebar.info("Use the options below to customize your view.")

# Main Title
st.title("📊 Beautiful Data Dashboard")

# Upload CSV
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    # Load Data
    df = pd.read_csv(uploaded_file)

    # Display Data Preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Sidebar Filters
    st.sidebar.subheader("Data Filters")
    numeric_columns = df.select_dtypes(include=["number"]).columns
    category_columns = df.select_dtypes(include=["object", "category"]).columns

    if not df.empty:
        with st.expander("🔍 Customize Data View"):
            # Fix: Convert df.columns to a list for options and default
            selected_columns = st.multiselect(
                "Select Columns", 
                options=list(df.columns), 
                default=list(df.columns[:5])  # Convert default to list
            )
            if selected_columns:
                st.write(df[selected_columns])

    # Visualization Options
    st.sidebar.subheader("Visualization")
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])
    x_axis = st.sidebar.selectbox("Select X-axis", numeric_columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", numeric_columns)

    if x_axis and y_axis:
        st.subheader(f"{chart_type}: {x_axis} vs {y_axis}")
        plt.figure(figsize=(10, 6))

        if chart_type == "Line Chart":
            plt.plot(df[x_axis], df[y_axis], marker="o", linestyle="-")
        elif chart_type == "Bar Chart":
            plt.bar(df[x_axis], df[y_axis], color="skyblue")
        elif chart_type == "Scatter Plot":
            plt.scatter(df[x_axis], df[y_axis], c="blue", alpha=0.7)

        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"{chart_type} of {x_axis} vs {y_axis}")
        st.pyplot(plt)

else:
    st.info("Please upload a CSV file to begin.")

st.markdown("developed by: Ingyete Jacob")
