import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


cars = ["fiat", 'ford', 'volvo', 'audi', 'mazda', 'bmw', 'toyota', 'toyota']
data = {
  "km": [20310, 12780, 40678, 15689, 25643, 38734, 30876, 30876],
  "h": [389, 200, 589, 248, 345, 489, 512, 512],
  'l/100km': [9.5, None, 12, 7.5, None, 8, 10.8, 10.8],
  "year": [2002, 2013, 2018, 2015, 2020, 2014, 2019, 2019],
  "date": ['2020/12/01', None, None, '2022/12/01', '2022/12/01', '2022/12/01', '2023/01/15', '2023/01/15']
}


pd.options.display.max_rows = 50

# Load data into a DataFrame object:
df = pd.DataFrame(data, index=cars)
print("Load data into a DataFrame object:")
print(df, '\n') 

# Handling dublicates rows
df.drop_duplicates(inplace = True)
print("Handling dublicates rows:\n", df, '\n') 

# Handling missing values
x = df["l/100km"].mean()
df["l/100km"] = df["l/100km"].fillna(x)
print("Handling missing values:")
print(df, '\n') 

# Calculate oil spent in liters for each car
df["oil_spent"] = (df["km"] / 100) * df["l/100km"]
print("Calculate oil spent in liters for each car:")
print(df, '\n') 

plt.bar(df.index, df["oil_spent"])
plt.xlabel("Cars")
plt.ylabel("Oil Spent (Liters)")
plt.title("Oil Consumption for Each Car")
plt.show()

print("Fiat details:")
print(df.loc['fiat'], '\n')

# Save DataFrame to CSV file
df.to_csv('cars_data.csv', index_label='car_name')

# Read CSV file
df_file = pd.read_csv('cars_data.csv')
print(df_file, '\n') 

# Row with Maximum 'km' value
max_km_index = df_file['km'].idxmax()
max_km_row = df_file.loc[max_km_index]
print("Row with Maximum 'km' value:")
print(max_km_row, '\n')

# швидкий огляд DataFrame 3 перших рядки
print("The first three and the last rows: ")
print(df_file.head(3))
print(df_file.tail(1), '\n') 

# All cars that spent more than the average amount of oil
print('All cars that spent more than the average amount of oil')
avg_oil_spent = df["oil_spent"].mean()
above_avg_df = df[df["oil_spent"] > avg_oil_spent]
print(above_avg_df)