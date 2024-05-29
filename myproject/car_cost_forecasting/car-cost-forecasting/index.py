import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np


class CarPricePredictor:
    def __init__(self, data):
        self.data = data
        self.model = None
        self.preprocessor = None

    def preprocess_data(self):
        # Preprocessing the data
        self.data['Latest_launch_year'] = pd.to_datetime(self.data['Latest_launch_year'], format='%d-%b-%y').dt.year

        X = self.data[['Brand', 'Model', 'Engine_size', 'Horsepower', 'Latest_launch_year']]
        y = self.data['Price']

        # Define preprocessing for numeric columns (scale them)
        numeric_features = ['Engine_size', 'Horsepower', 'Latest_launch_year']
        numeric_transformer = StandardScaler()

        # Define preprocessing for categorical features (encode them)
        categorical_features = ['Brand', 'Model']
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        # Create preprocessor
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        return X, y

    def train_model(self):
        X, y = self.preprocess_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train the model pipeline
        self.model = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('regressor', LinearRegression())
        ])

        self.model.fit(X_train, y_train)
        print(f'Model training completed. R^2 score on test data: {self.model.score(X_test, y_test)}')

    def predict_price(self, brand, model, engine_size, horsepower, latest_launch_year):
        car_features = pd.DataFrame({
            'Brand': [brand],
            'Model': [model],
            'Engine_size': [engine_size],
            'Horsepower': [horsepower],
            'Latest_launch_year': [latest_launch_year]
        })

        car_features['Latest_launch_year'] = pd.to_datetime(car_features['Latest_launch_year'], format='%Y').dt.year

        # Transform the features using the preprocessor
        transformed_features = self.preprocessor.transform(car_features)
        predicted_price = self.model.named_steps['regressor'].predict(transformed_features)
        return predicted_price[0]


data = pd.read_csv('Cleaned_Car_Sales_Data.csv')
predictor = CarPricePredictor(data)
predictor.train_model()
predicted_price = predictor.predict_price('Audi', 'A4', 2.0, 200, '2015')
print(f'Predicted Price: {predicted_price}')
