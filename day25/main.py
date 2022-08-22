# from pandas import DataFrame

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.DictReader(data_file)
#     temperatures = []
    
#     for row in data:
#         print(row)
#         temperatures.append(int(row['temp']))

#     print(temperatures)


import pandas as pd

# data = pandas.read_csv("weather_data.csv")

# temp_list = data['temp'].to_list()
# print(temp_list)
# print(f"Mean temp is: {data['temp'].mean()}")
# print(f"Max temp is: {data['temp'].max()}")
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])

# monday_temp_c = data[data.day == 'Monday'].temp
# print(f"Monday's temp in Celsius: {monday_temp_c}")
# print(f"Monday's temp in Farenheit: {(monday_temp_c * 9 / 5) + 32}")

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cd = df['Primary Fur Color'].value_counts().to_dict()

count_df = pd.DataFrame({'Fur Color': cd.keys(), 'Count': cd.values()})

count_df.to_csv("squirrel_count.csv")

# count_series.to_csv("squirrel_count.csv")
# by_color = df.groupby(by='Primary Fur Color')
# print(f"Colors: {by_color.get_group('Primary Fur Color').tolist()}; Count: {by_color['Primary Fur Color'].count()}")


