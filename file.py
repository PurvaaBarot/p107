from turtle import color
import pandas as pd
import plotly_express as px


df=pd.read_csv("Book1.csv")

fig=px.scatter(df , x= "Marks In Percentage" , y="Days Present" ,  color="Roll No")
fig.show()