import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np



class CarPricePredictor:
    def __init__(self):
        self.data = pd.read_csv('Cleaned_Car_Sales_Data.csv')
        self.model = None
        self.preprocessor = None
        self.train_model()


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

        # LinearRegression
        # self.model = Pipeline(steps=[
        #     ('preprocessor', self.preprocessor),
        #     ('regressor', LinearRegression())
        # ])
        # DecisionTreeRegressor
        # self.model = Pipeline(steps=[
        #     ('preprocessor', self.preprocessor),
        #     ('regressor', DecisionTreeRegressor(random_state=42))
        # ])
        # RandomForestRegressor
        # self.model = Pipeline(steps=[
        #     ('preprocessor', self.preprocessor),
        #     ('regressor', RandomForestRegressor(random_state=42))
        # ])
        # GradientBoostingRegressor
        # self.model = Pipeline(steps=[
        #     ('preprocessor', self.preprocessor),
        #     ('regressor', GradientBoostingRegressor(random_state=42))
        # ])
        # SVR
        # self.model = Pipeline(steps=[
        #     ('preprocessor', self.preprocessor),
        #     ('regressor', SVR(kernel='rbf'))
        # ])
        # KNeighborsRegressor
        # self.model = Pipeline(steps=[
        #     ('preprocessor', self.preprocessor),
        #     ('regressor', KNeighborsRegressor())
        # ])
        # Ridge
        self.model = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('regressor', Ridge())
        ])
        # Lasso
        # self.model = Pipeline(steps=[
        #     ('preprocessor', self.preprocessor),
        #     ('regressor', Lasso())
        # ])
        # ElasticNet
        # self.model = Pipeline(steps=[
        #     ('preprocessor', self.preprocessor),
        #     ('regressor', ElasticNet())
        # ])

        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        print("Model: Ridge")
        print(f'R^2 score on test data: {r2_score(y_test, y_pred)}')
        print(f'Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred)}')
        print(f'Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred)}')
        print(f'Root Mean Squared Error (RMSE): {np.sqrt(mean_squared_error(y_test, y_pred))}')
        print(f'Model training completed.')


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



predictor = CarPricePredictor()
predicted_price = predictor.predict_price('Audi', 'A4', 2.0, 200, '2015')
print(f'Predicted Price: {predicted_price}')
