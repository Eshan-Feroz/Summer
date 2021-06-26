import pandas as pd
import plotly.express as px
import numpy as np
import csv

#df = pd.read_csv("icecream.csv")
cooldrinkSales = []
icecreamSales = []
temperature = []
def getData(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        for i in reader:
            icecreamSales.append(float(i["Ice-cream Sales( ₹ )"]))
            temperature.append(float(i["Temperature"]))
            cooldrinkSales.appens(float(i["Cold drink sales( ₹ )"]))
    return({
        "x": temperature,
        "y": cooldrinkSales
    })

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("The correlation between the two dataset is " + str(correlation))

def main():
    path = "icecream.csv"
    dataSource = getData(path)
    findCorrelation(dataSource)
main()



