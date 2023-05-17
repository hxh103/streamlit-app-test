import streamlit as st

st.title('This is title')
st.header('header')
st.text('text')

st.text('🥣 🥗 🐔 🥑🍞')

import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
st.dataframe(my_fruit_list)
