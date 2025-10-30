# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Gapminder Plotly Demo", layout="centered")

# Title
st.title('🌍 Using Plotly Graphs in Streamlit')

# Load dataset
df = px.data.gapminder()

# Preview data
with st.expander("🔍 View Raw Data"):
    st.write(df.head())

# Plotting animated scatter plot
st.subheader("📈 Animated GDP vs Life Expectancy by Year")

fig = px.scatter(
    df, 
    x='gdpPercap', 
    y='lifeExp', 
    size='pop', 
    color='continent', 
    hover_name='country', 
    log_x=True, 
    size_max=60, 
    animation_frame="year", 
    animation_group="country",
    title="GDP per Capita vs Life Expectancy (1952 - 2007)"
)

fig.update_layout(width=800, height=500)
st.plotly_chart(fig)
