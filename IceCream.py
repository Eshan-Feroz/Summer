import pandas as pd
import plotly.express as px
import csv

dataFrame = pd.read_csv("icecream.csv")
fig = px.scatter(dataFrame, x = "Temperature", y = "Ice-cream Sales( ₹ )" )
fig.show()