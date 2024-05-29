import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import VotingRegressor
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
        self.data['Car_Age'] = 2024 - self.data['Latest_launch_year']  

        X = self.data[['Brand', 'Model', 'Engine_size', 'Horsepower', 'Car_Age']]
        y = self.data['Price']

        # Define preprocessing for numeric columns (scale them)
        numeric_features = ['Engine_size', 'Horsepower', 'Car_Age']
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

        self.preprocessor.fit(X_train)

        kneighbors = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('regressor', KNeighborsRegressor())
        ])

        ridge = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('regressor', Ridge())
        ])

        self.model = VotingRegressor(estimators=[
            ('ridge', ridge),
            ('kn', kneighbors)
        ])

        # Hyperparameter Tuning
        # Using Grid Search to find the best hyperparameters for Ridge Regression:
        # don't work
        # param_grid = {
        #     'regressor__alpha': [0.1, 1.0, 10.0],
        #     'regressor__solver': ['auto', 'svd', 'cholesky', 'lsqr', 'sag']
        # }
        # grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='r2')
        # grid_search.fit(X_train, y_train)
        # self.model = grid_search.best_estimator_

        cv_scores = cross_val_score(self.model, X, y, cv=5, scoring='r2')

        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print("Model: Ridge with Cross-Validation")
        print(f'Cross-validated R^2 scores: {cv_scores}')
        print(f'Average R^2 score: {np.mean(cv_scores)}')
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
        car_features['Car_Age'] = 2024 - car_features['Latest_launch_year']
        car_features = car_features.drop(columns=['Latest_launch_year'])

        predicted_price = self.model.predict(car_features)
        return predicted_price[0]



predictor = CarPricePredictor()
predicted_price = predictor.predict_price('Audi', 'A4', 2.0, 200, '2015')
print(f'Predicted Price: {predicted_price}')
