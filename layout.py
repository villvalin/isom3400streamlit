import streamlit as st
import time

st.title("Business Performance Dashboard")
st.write("Objective: Provide insights into revenue, customer feedback, and market trends.")

col1, col2, col3 = st.columns(3)
with col1:
    st.header("Q1 2024")
    st.write("Revenue: $1.2M")

with col2:
    st.header("Q2 2024")
    st.write("Revenue: $1.5M")
with col3:
    st.header("Q3 2024")
    st.write("Revenue: $1.3M")
  

tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])
with tab1:
    st.write("Content for Sales Data")
    sales_data={
        "Q1":"1.2M",
        "Q2":"1.5M",
        "Q3":"1.3M",
        "Q4":"1.6M"
  }
    for q,s in sales_data.items():
        print(f"{q}:{s}")

with tab2:
    st.write("Content for Customer insights")
    feedbacks=["Best service", "Fast delivery", "Nice"]
    for feedback in feedbacks:
        print(feedback)
  

with tab3:
    st.write("Content for market trend")
    trends=["Upword", "Downward","Stagnant"]
    for trend in trends:
        print(trend)

with st.expander("More Information"):
    st.write("Data collected via surveys and reports.")

selected_quarter = st.selectbox("Select a quarter:", ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"])
sales_data={
    "Q1":"1.2M",
    "Q2":"1.5M",
    "Q3":"1.3M",
    "Q4":"1.6M"
  }
if selected_quarter=="Q1 2024":
  print(sales_data["Q1"])
elif selected_quarter=="Q2 2024":
  print(sales_data["Q2"])
elif selected_quarter=="Q3 2024":
  print(sales_data["Q3"])
elif selected_quarter=="Q4 2024":
  print(sales_data["Q4"])

growth = st.slider("Adjust growth percentage:", 0, 50, 10)


placeholder = st.empty()
for i in range(5):
    placeholder.write(f"Loading data... {i*20}% complete")
    time.sleep(1)
placeholder.write("Data loading complete!")

st.bar_chart({"Revenue (in M$)": [1.2, 1.5, 1.3, 1.6]})
if st.button("Show Motivation"):
    st.success("Keep pushing for growth! 🚀")
