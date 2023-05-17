import streamlit as st

st.title('This is title')
st.header('header')
st.text('text')

st.text('🥣 🥗 🐔 🥑🍞')
st.header('🥣 🥗 Build your own fruit smoothie 🐔 🥑🍞')
import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

st.multiselect("Pick some fruit: ", list(my_fruit_list.index), ['Avocado','Strawberries')
st.dataframe(my_fruit_list)
