import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Retail Business Dashboardf")
st.header("Manager Input Selection")
st.write("Please enter the monthly sales target and select the region")

sales=st.number_input("Enter monthly sales target (in USD)")
region=st.selectbox("Select region:",["North","South","East"])

if st.button("Submit"):
  st.success(f"Your target is {sales} in {region})
      
