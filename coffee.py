import csv
import pandas as pd
import plotly.express as px
#with open("Coffee.csv") as f:
    #df = csv.DictReader(f)

df = pd.read_csv("Coffee.csv")


fig = px.scatter(df, x ="Coffee in ml", y ="sleep in hours", color ="week")
fig.show()

#print(df[0])
