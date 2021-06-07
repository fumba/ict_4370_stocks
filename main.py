import matplotlib.pyplot as plt, mpld3
import json
from datetime import datetime
from collections import defaultdict
from database import Database


# open json file containing data
file = open('AllStocks.json')

# JSON object as a dictionary
data = json.load(file)

# Prepare plot data
x_axis_array=  []

# extract close value and date based on stock symbol
plot_data = {}
plot_data = defaultdict(lambda: [], plot_data) #set the default for all symbols to []
for row in data:
    date_dt = datetime.strptime(row['Date'], '%d-%b-%y') # this matches date format provided in JSON
    plot_data[row['Symbol']].append([date_dt, row['Close'] * row['Volume']])

# save to database
Database(plot_data).createDB();

# plot each stock symbol
plot_width = 50
plot_height = 30
dots_per_inch = 70
plt.figure(figsize=(plot_width, plot_height), dpi=dots_per_inch)
plt.rcParams.update({'font.size': 22})
for symbol,array_values in plot_data.items():
    x = []
    y = []
    for array_value in array_values:
        x.append(array_value[0]) # datetime
        y.append(array_value[1]) # symbol_close_calculation
    plt.plot(x, y, label=symbol)
    plt.legend()
plt.savefig("out.png")
mpld3.show()
