# tests/test_predictive_analysis.py

import unittest
import pandas as pd
from src.predictive_analysis.models import SalesPredictor
from src.predictive_analysis.simulator import ScenarioSimulator

class TestPredictiveAnalysis(unittest.TestCase):
    """Testes para o módulo de análises preditivas."""

    def setUp(self):
        """Configura o ambiente de teste."""
        # Cria um conjunto de dados sintético para os testes.
        self.test_data = pd.DataFrame({
            'preco': [10, 12, 11, 15, 9],
            'marketing': [100, 150, 120, 200, 80],
            'vendas': [50, 60, 55, 75, 45]
        })
        self.features = self.test_data[['preco', 'marketing']]
        self.target = self.test_data['vendas']
        self.model = SalesPredictor()
        self.model.train(self.features, self.target)

    def test_sales_predictor_train(self):
        """Testa o treinamento do modelo de previsão de vendas."""
        self.assertIsNotNone(self.model.model.coef_)

    def test_sales_predictor_predict(self):
        """Testa a predição do modelo."""
        predictions = self.model.predict(self.features)
        self.assertEqual(len(predictions), 5)

    def test_scenario_simulator(self):
        """Testa o simulador de cenários."""
        simulator = ScenarioSimulator(self.model, self.test_data)
        result = simulator.run_simulation('preco', 0.1) # Aumento de 10% no preço
        self.assertIn('impact', result)
        self.assertNotEqual(result['impact'], 0)

if __name__ == '__main__':
    unittest.main()
