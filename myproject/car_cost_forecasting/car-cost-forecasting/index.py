from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd



class CarPricePredictor:
    def __init__(self):
        self.data = pd.read_csv('Cleaned_Car_Sales_Data.csv')
        self.model = None
        self.preprocessor = self._create_preprocessor()
        self._train_model()


    # внутрішній метод попередньої обробки даних
    def _create_preprocessor(self):
        # стандартизація числових даних (об'єм двигуна, кінські сили, вік авто)
        numeric_features = ['Engine_size', 'Horsepower', 'Car_Age']
        numeric_transformer = StandardScaler()

        # обробка категоріальних даних (модель, бренд)
        categorical_features = ['Brand', 'Model']
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ]
        )
        return preprocessor


    # внутрішній метод конфігурації параметрів 
    def _preprocess_data(self):
        self.data['Latest_launch_year'] = pd.to_datetime(self.data['Latest_launch_year'], format='%d-%b-%y').dt.year
        self.data['Car_Age'] = 2024 - self.data['Latest_launch_year']

        X = self.data[['Brand', 'Model', 'Engine_size', 'Horsepower', 'Car_Age']]
        y = self.data['Price']
        return X, y


    # внутрішній метод конфігурації конвеєрів для моделі
    def _create_pipelines(self):
        kneighbors = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('regressor', KNeighborsRegressor())
        ])

        ridge = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('regressor', Ridge())
        ])

        return kneighbors, ridge


    # внутрішній метод навчання моделі
    def _train_model(self):
        # попередня обробка даних для тренування і тестування
        X, y = self._preprocess_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # навчання попереднього оброблювача даних
        self.preprocessor.fit(X_train)

        # створення комбінована моделі 
        kneighbors, ridge = self._create_pipelines()
        self.model = VotingRegressor(estimators=[
            ('ridge', ridge),
            ('kn', kneighbors)
        ])

        # перехресна валідація
        cv_scores = cross_val_score(self.model, X, y, cv=5, scoring='r2')

        # навчання моделі
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)

        # оцінка точності моделі (0.72)
        self._print_metrics(y_test, y_pred, cv_scores)


    # внутрішній метод 
    def _print_metrics(self, y_test, y_pred, cv_scores):
        print("Model: Voting Regressor with Ridge and KNeighbors")
        print(f'Cross-validated R^2 scores: {cv_scores}')
        print(f'Average R^2 score: {np.mean(cv_scores)}')
        print(f'R^2 score on test data: {r2_score(y_test, y_pred)}')
        print(f'Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred)}')
        print(f'Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred)}')
        print(f'Root Mean Squared Error (RMSE): {np.sqrt(mean_squared_error(y_test, y_pred))}')
        print('Model training completed.')


    # метод прогнозування ціни авто в залежності від заданих параметрів
    def predict_price(self, brand, model, engine_size, horsepower, latest_launch_year):
        car_features = pd.DataFrame({
            'Brand': [brand],
            'Model': [model],
            'Engine_size': [engine_size],
            'Horsepower': [horsepower],
            'Latest_launch_year': [latest_launch_year]
        })

        # з інформації про рік випуску машини дізнаємося дані про її вік
        car_features['Latest_launch_year'] = pd.to_datetime(car_features['Latest_launch_year'], format='%Y').dt.year
        car_features['Car_Age'] = 2024 - car_features['Latest_launch_year']
        car_features = car_features.drop(columns=['Latest_launch_year'])

        # прогнозуємо ціну за відповідними параметрами
        transformed_features = self.preprocessor.transform(car_features)
        predicted_price = self.model.predict(transformed_features)
        return predicted_price[0]



# predictor = CarPricePredictor()
# predicted_price = predictor.predict_price('Audi', 'A4', 2.0, 200, '2015')
# print(f'Predicted Price: {predicted_price}')
