import statistics as st
import matplotlib.pyplot as plt
import io
import base64
def calculate_metrics(date_dicts,start_date,end_date):
    values=[]
    overall={}
    for date,data in date_dicts.items():
        if start_date<= date <= end_date:
           info={}
           info["open"]=data['1. open'];
           info["high"]=data['2. high'];
           info["low"]=data['3. low'];
           info["close"]=data['4. close'];

           value=(float(data['2. high'])+float(data['3. low']))/2
           info["mean"]=value
           overall[date]=info
           values.append(value)
    
    if not values:
        raise ValueError("No data available for the specified dates and metric")
    mean=st.mean(values)
    median=st.median(values)
    variance=st.variance(values)
    plt.figure(figsize=(8, 6))
    plt.xlim(left=-5, right=5)
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.axvline(mean, color='blue', linestyle='dashed', linewidth=1, label=f'Mean: {mean:.2f}')
    plt.axvline(median, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median:.2f}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram with Mean and Median')
    # plt.legend()
    # Convert the plot to base64
    plt.tight_layout()
    plt.show();
    plt.bar(mean, median)
    plt.xlabel('mean')
    plt.ylabel('median')
    plt.title('Bar Plot')
    plt.show()
    return mean, median, variance, overall