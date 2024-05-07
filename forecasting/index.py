import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore')

# Завантаження даних
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

# Fit ARIMA model
model = ARIMA(df['traffic'], order=(6, 1, 0))
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Diagnostic plots
residuals = model_fit.resid
fig, ax = plt.subplots(1, 3, figsize=(15, 5))  
plot_acf(residuals, ax=ax[0])
plot_pacf(residuals, ax=ax[1])
ax[2].plot(df['Date'], df['traffic'].diff(1))  # Plot differenced series to check for trend
ax[2].set_title("Differenced Series (lag=1)")
plt.show()

# Seasonal decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['traffic'], model='additive', period=30)  # Assuming a period of 30 days
result.plot()
plt.show()
