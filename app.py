import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv("energy.csv")

# Title
st.title("🌍 Global Energy Consumption Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

country = st.sidebar.selectbox(
    "Select Country",
    data["country"].unique()
)

# Filtered data
filtered = data[data["country"] == country]

# 🔹 Line Chart (Energy Trend)
st.subheader("📈 Energy Consumption Over Time")
fig1 = px.line(filtered, x="year", y="energy", markers=True)
st.plotly_chart(fig1)

# 🔹 Bar Chart (Top Countries)
st.subheader("📊 Top Energy Consuming Countries")
top = data.groupby("country")["energy"].sum().reset_index()
top = top.sort_values(by="energy", ascending=False)

fig2 = px.bar(top, x="country", y="energy")
st.plotly_chart(fig2)

# 🔹 Pie Chart (Energy Share)
st.subheader("🥧 Energy Share by Country")
fig3 = px.pie(top, names="country", values="energy")
st.plotly_chart(fig3)

# 🔹 Renewable vs Total
st.subheader("🌱 Renewable Energy Growth")
fig4 = px.line(filtered, x="year", y=["energy", "renewables"], markers=True)
st.plotly_chart(fig4)

# 🔹 Map Visualization
st.subheader("🗺️ Global Energy Map")
latest = data[data["year"] == data["year"].max()]

fig5 = px.choropleth(
    latest,
    locations="country",
    locationmode="country names",
    color="energy",
    title="Energy Consumption by Country"
)
st.plotly_chart(fig5)

st.success("Dashboard Loaded Successfully ✅")