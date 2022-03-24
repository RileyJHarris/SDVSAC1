import pandas as pd
import os

#load csv
dat = pd.read_csv('dat.csv')

#calculate profit on each sale
dat["Profit"] = dat["Sale price"] - dat["Purchase price"]
#set profit = 0 for all unsold items
dat["Profit"] = dat["Profit"].fillna(0)
#sum profit
TotalProfit = dat["Profit"].sum()

#iterate rows and display title and profit
for index, row in dat.iterrows():
    print("Book Title: ", row["Textbook"], "  profit made: ", row["Profit"])
print("Total Profit: ", TotalProfit)