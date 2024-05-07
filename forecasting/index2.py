import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
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
model = ARIMA(train, order=(5, 1, 0))
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Diagnostic plots
residuals = model_fit.resid
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
plot_acf(residuals, ax=ax[0])
plot_pacf(residuals, ax=ax[1])
plt.show()

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
