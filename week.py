# import requests, json
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=0PHRHEAR6E3UPIQ6'
# r = requests.get(url)
# dat = r.json()
from collections import defaultdict
import statistics as st
import json
import os
import calculate
import _strptime
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
file_path='data.json'

with open(file_path, "r") as file:
    data = json.load(file)

daily_time_series=data["Time_Series"]

date_dicts = {}
for date, values in daily_time_series.items():
    date_dicts[date] = values
# print(date_dicts)
# Print the dictionaries
# for date, data in date_dicts.items():
#     print(f"Data for {date}: {data}")

# start_date = input("Please enter a start date (in YYYY-MM-DD format): ")

# end_date = input("Please enter a end date (in YYYY-MM-DD format): ")
# metric = input("Enter the metric:")
# print(date_dicts)
def calculate_monthly_means(date_dicts):
    monthly_means = defaultdict(list)
    for key, values in date_dicts.items():
        # print(key,date_dicts[key])
        year_month = datetime.strptime(key, '%Y-%m-%d').strftime('%Y-%m')
        open_price = float(values["1. open"])
        monthly_means[year_month].append(open_price)
    # return "hello"
    return {month: np.mean(prices) for month, prices in monthly_means.items()}
def plot_monthly_means():
    monthly_means = calculate_monthly_means(date_dicts)
    months = list(monthly_means.keys())
    means = list(monthly_means.values())
    # plt.figure(figsize=(10, 6))
    plt.bar(months, means, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Mean Open Price')
    plt.title('Mean Open Price by Month')
    # plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def calculate_values(start_date,end_date):
    mean,median,variance, overall=calculate.calculate_metrics(date_dicts,start_date,end_date)
    values={}
    values['mean']=mean
    values['median']=median
    values['variance']=variance
    return values, overall

