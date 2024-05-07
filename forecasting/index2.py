import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv('data.csv', parse_dates=[0])

# Plot site activity
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['traffic'], label='Traffic')
plt.plot(df['Date'], df['leads'], label='Leads')
plt.plot(df['Date'], df['actions'], label='Actions')
plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Site Activity")
plt.legend()
plt.show()

# Train-test split
train_size = int(len(df) * 0.8)
train, test = df['traffic'][:train_size], df['traffic'][train_size:]

# Fit ARIMA model
model = ARIMA(train, order=(3, 1, 0))
model_fit = model.fit()

# Forecast
forecast = model_fit.forecast(len(test))

# Calculate Mean Squared Error
mse = mean_squared_error(test, forecast)
print(f"Mean Squared Error: {mse}")

# Plot forecast vs actuals
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['traffic'], label='Actual')
plt.plot(df.index[train_size:], forecast, label='Forecast', color='red')
plt.xlabel("Date")
plt.ylabel("Traffic")
plt.title("ARIMA Forecast vs Actual")
plt.legend()
plt.show()
