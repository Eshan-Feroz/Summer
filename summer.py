import csv
import pandas as pd
import plotly.express as px
import numpy as np

def readData(dataFile):
    with open(dataFile) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales( ₹ )")
        fig.show()

readData("icecream.csv")
