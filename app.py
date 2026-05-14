import streamlit as st
import pandas as pd

# Load movie name data (Excel file)
data = pd.read_excel(r"Movie_Name.xlsx")

st.title("🎬 Movie Recommendation System")

# Show dataset
if st.checkbox("Show all movies"):
    st.write(data)

# Select category
genre = st.selectbox(
    "Select movie Genre",
    data["Genre"].unique()
)

# Initialize result as empty DataFrame
result = pd.DataFrame()

# Recommendation Button
if st.button("Recommended Movies"):
    result = data[data["Genre"] == genre]

# Display recommendations only if result is not empty
if not result.empty:
    st.subheader("Recommended Movies")
    for movie in result["Movie Name"]:
        st.write(movie)
