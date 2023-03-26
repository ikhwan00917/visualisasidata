import pandas as pd
import plotly.figure_factory as ff
import streamlit as st

df = pd.read_excel(r"C:\IKHWAN\Tel U\SEMESTER 4\Metode Visualisasi Data\factbook2.xlsx")

fig = ff.scatter(df, x = "GDPpercapita", y = "Lifeexpectancyatbirth",
            size="Population", color = "Birthrate",
            hover_name="Country", log_x = True, size_max =60)
st.plotly_chart(fig, height = 1000, width = 1200)
