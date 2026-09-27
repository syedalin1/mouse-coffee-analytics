# Import the libraries
import streamlit as st
import pandas as pd

# App title
st.title("Mouse Coffee Analytics")

# Explain what the app does
st.write("Upload your coffee shop Excel file to analyse the data.")

# Create an Excel upload button
uploaded_file = st.file_uploader(
    "Upload your Excel file",
    type=["xlsx"]
)

# Run this section after a file is uploaded
if uploaded_file is not None:

    # Read the Excel file
    df = pd.read_excel(uploaded_file)

    # Confirm the upload worked
    st.success("File uploaded successfully!")

    # Show the first 10 rows
    st.subheader("Data Preview")
    st.dataframe(df.head(10))
