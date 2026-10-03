import streamlit as st
import pandas as pd

st.title("🌱 Ingredients Network Dashboard")
st.write("This web application displays the scraped and cleaned data from IngredientsNetwork.com as part of the hiring challenge.")

# Load the cleaned CSV file
df = pd.read_csv("ingredients_results.csv")

# Display total count metrics
st.metric(label="Total Records Extracted", value=len(df))

# Show data in a clean, readable tabular format
st.subheader("Extracted Company & Ingredient Data")
st.dataframe(df)
