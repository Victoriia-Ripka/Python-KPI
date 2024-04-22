import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import warnings
warnings.filterwarnings('ignore')

# Завантаження даних
df = pd.read_csv('./df.csv', parse_dates=True, index_col='car_name')

# Припустимо, що у нас є DataFrame з іменем df
df['km'].plot()
plt.show()

# Налаштування моделі ARIMA
model = ARIMA(df['km'], order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# Прогнозування
forecast = model_fit.forecast(steps=6)
print(forecast)
