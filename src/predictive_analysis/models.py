# src/predictive_analysis/models.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

class BaseModel:
    """Classe base para os modelos de machine learning."""

    def __init__(self):
        self.model = None

    def train(self, X, y):
        """Treina o modelo."""
        raise NotImplementedError

    def predict(self, X):
        """Faz previsões com o modelo treinado."""
        raise NotImplementedError

    def evaluate(self, X_test, y_test):
        """Avalia a performance do modelo."""
        predictions = self.predict(X_test)
        return self._calculate_metrics(y_test, predictions)

    def _calculate_metrics(self, y_true, y_pred):
        """Calcula as métricas de avaliação."""
        raise NotImplementedError


class SalesPredictor(BaseModel):
    """Modelo para prever vendas."""

    def __init__(self):
        super().__init__()
        self.model = LinearRegression()

    def train(self, features, target):
        """Treina o modelo de regressão linear."""
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        print("Modelo de previsão de vendas treinado.")
        print("Avaliando o modelo...")
        self.evaluate(X_test, y_test)

    def predict(self, X):
        """Faz previsões de vendas."""
        return self.model.predict(X)

    def _calculate_metrics(self, y_true, y_pred):
        """Calcula o erro quadrático médio."""
        mse = mean_squared_error(y_true, y_pred)
        print(f"Mean Squared Error: {mse}")
        return mse
