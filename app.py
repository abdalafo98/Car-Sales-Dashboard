import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.title("Car Sales Dashboard")
st.header("Explore Car Sales Data")

st.subheader("Car Price Distribution")
fig_hist = px.histogram(df, x="price", nbins=50, title="Car Price Distribution")
st.plotly_chart(fig_hist)

st.subheader("Odometer vs. Price")
fig_scatter = px.scatter(df, x="odometer", y="price", title="Odometer vs. Price",
                         labels={"odometer": "Odometer (miles)", "price": "Price ($)"},
                         color="condition", hover_data=["model", "model_year"])
st.plotly_chart(fig_scatter)

if st.checkbox("Show only vehicles with odometer readings"):
    df_filtered = df.dropna(subset=["odometer"])
    fig_scatter_filtered = px.scatter(df_filtered, x="odometer", y="price",
                                      title="Odometer vs. Price (Filtered)",
                                      labels={"odometer": "Odometer (miles)", "price": "Price ($)"},
                                      color="condition", hover_data=["model", "model_year"])
    st.plotly_chart(fig_scatter_filtered)
