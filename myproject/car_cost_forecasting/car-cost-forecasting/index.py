import pandas as pd
from sklearn.linear_model import LinearRegression


class CarPricePredictor:
    def __init__(self, data):
        self.data = data
        self.model_current_price = None
        self.model_resale_price = None
        self._train_models()

    def _train_models(self):
        # Prepare the data
        X = self.data[['Brand', 'Model', 'Engine_size', 'Horsepower', 'Latest_launch_year']]
        X = pd.get_dummies(X, columns=['Brand', 'Model', 'Latest_launch_year'])
        y_current_price = self.data['Price']
        y_resale_price = self.data['4_year_resale_value']

        # Train model for current price
        self.model_current_price = LinearRegression()
        self.model_current_price.fit(X, y_current_price)

        # Train model for resale price
        self.model_resale_price = LinearRegression()
        self.model_resale_price.fit(X, y_resale_price)

    def predict_current_price(self, brand, model, engine_size, horsepower, latest_launch_year):
        input_data = pd.DataFrame([[brand, model, engine_size, horsepower, latest_launch_year]],
                                  columns=['Brand', 'Model', 'Engine_size', 'Horsepower', 'Latest_launch_year'])
        input_data = pd.get_dummies(input_data, columns=['Brand', 'Model', 'Latest_launch_year'])
        input_data = input_data.reindex(columns=self.model_current_price.feature_names_in_, fill_value=0)

        return self.model_current_price.predict(input_data)[0]

    def predict_resale_price(self, brand, model, engine_size, horsepower, latest_launch_year):
        input_data = pd.DataFrame([[brand, model, engine_size, horsepower, latest_launch_year]],
                                  columns=['Brand', 'Model', 'Engine_size', 'Horsepower', 'Latest_launch_year'])
        input_data = pd.get_dummies(input_data, columns=['Brand', 'Model', 'Latest_launch_year'])
        input_data = input_data.reindex(columns=self.model_resale_price.feature_names_in_, fill_value=0)

        return self.model_resale_price.predict(input_data)[0]


# Пример использования:
# Загружаем очищенные данные
df_cleaned = pd.read_csv('Cleaned_Car_Sales_Data.csv')

# Создаем экземпляр класса
predictor = CarPricePredictor(df_cleaned)

# Прогнозируем текущую цену и цену через 4 года
current_price = predictor.predict_current_price('Chevrolet', 'Camaro', 3.8, 200, '23-Oct-15')
resale_price = predictor.predict_resale_price('Chevrolet', 'Camaro', 3.8, 225, '23-Oct-15')

print(f"Current Price: {current_price}")
print(f"Resale Price: {resale_price}")


#23,Chevrolet,Camaro,3.8,200,23-Oct-15,24.34,13.025