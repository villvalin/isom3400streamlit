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
        st.write(f"{q}:{s}")

with tab2:
    st.write("Content for Customer insights")
    feedbacks=["Best service", "Fast delivery", "Nice"]
    for feedback in feedbacks:
        st.write(feedback)
  

with tab3:
    st.write("Content for market trend")
    trends=["Upword", "Downward","Stagnant"]
    for trend in trends:
        st.write(trend)

with st.expander("More Information"):
    st.write("Data collected via surveys and reports.")

selected_quarter = st.selectbox("Select a quarter:", ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"])
sales_data={
    "Q1":"1.2M",
    "Q2":"1.5M",
    "Q3":"1.3M",
    "Q4":"1.6M"
  }
with selected_quarter=="Q1 2024":
  st.write(sales_data["Q1"])
with selected_quarter=="Q2 2024":
  st.write(sales_data["Q2"])
with selected_quarter=="Q3 2024":
  st.write(sales_data["Q3"])
with selected_quarter=="Q4 2024":
  st.write(sales_data["Q4"])

selected_quarter = st.selectbox(
    "Select a quarter:", list(sales_data.keys())

base_rev = sales_data[selected_quarter]
updated_rev = base_rev * (1 + growth / 100)

st.subheader("Selected Quarter Details")
st.write(f"Base revenue for {selected_quarter}: **${base_rev:.1f}M**")
st.write(f"Revenue after **{growth}%** growth: **${updated_rev:.2f}M**")

# --- Apply growth to all quarters for the bar chart ---
base_values = list(sales_data.values())
updated_values = [rev * (1 + growth / 100) for rev in base_values]

df = pd.DataFrame(
    {"Quarter": list(sales_data.keys()), "Revenue (M$)": updated_values}
).set_index("Quarter")

st.subheader("Revenue by Quarter (with growth applied)")
st.bar_chart(df)

placeholder = st.empty()
for i in range(5):
    placeholder.write(f"Loading data... {i*20}% complete")
    time.sleep(1)
placeholder.write("Data loading complete!")

st.bar_chart({"Revenue (in M$)": [1.2, 1.5, 1.3, 1.6]})
if st.button("Show Motivation"):
    st.success("Keep pushing for growth! 🚀")
