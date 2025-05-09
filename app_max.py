
import streamlit as st
import pandas as pd
import altair as alt

# Load the data
df = pd.read_csv("hourly_usage_data_max.csv")

st.title("Electricity Usage Dashboard")
st.markdown("Visualize **maximum hourly electricity consumption** across months.")

# Month selector
month_selected = st.selectbox("Select Month", sorted(df['Month'].unique()))

# Filtered data
df_month = df[df["Month"] == month_selected]

# Altair chart
chart = alt.Chart(df_month).mark_line(point=True).encode(
    x=alt.X("Hour:O", title="Hour of Day"),
    y=alt.Y("kWh:Q", title="Max Energy Consumption (kWh)"),
    tooltip=["Date/Time", "Hour", "kWh"]
).properties(
    title=f"Max Hourly Electricity Usage - {month_selected}",
    width=700,
    height=400
).interactive()

st.altair_chart(chart, use_container_width=True)

# Aggregate stats
st.subheader("Monthly Stats")
total_kwh = df_month["kWh"].sum()
peak_hour = df_month.groupby("Hour")["kWh"].max().idxmax()
st.metric(label="Total of Max Hourly Values", value=f"{total_kwh:.2f} kWh")
st.metric(label="Hour with Highest Max Usage", value=f"{peak_hour}:00")
