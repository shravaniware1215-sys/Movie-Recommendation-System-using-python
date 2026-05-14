import streamlit as st
import pandas as pd

#Load movie name data(exelfile)
data = pd.read_excel(r"Movie_Name.xlsx")

st.title("🎬Movie Recommendation System")

#show dataset
if st.checkbox("Show all movies"):
    st.write(data)

#select catagery
genre = st.selectbox(
    "select movie Genre",
    data["Genre"].unique()
)
#Recommendetion Button
if st.button("Recommended Movies"):
    result = data[data["Genre"]==genre]

st.subheader("Recommended Movie")

for movie in result["Movie Name"]:
    st.write(movie)