# tests/test_agents.py

import unittest
from unittest.mock import MagicMock
from src.agents.base_agent import BaseAgent
from src.assistant.assistant_agent import AssistantAgent
from src.reports.report_agent import ReportAgent
from src.predictive_analysis.prediction_agent import PredictionAgent
import pandas as pd

class MockBaseAgent(BaseAgent):
    """
    Mock do BaseAgent para testes.
    """
    def __init__(self, api_key="test_key"):
        super().__init__(api_key)
        self.response = "Mocked response"

    def generate_response(self, prompt):
        return self.response

class TestSpecializedAgents(unittest.TestCase):
    """
    Testes para os agentes especializados.
    """

    def setUp(self):
        """
        Configura um mock do BaseAgent para cada teste.
        """
        self.mock_base_agent = MockBaseAgent()

    def test_assistant_agent(self):
        """
        Testa o AssistantAgent com o mock do BaseAgent.
        """
        self.mock_base_agent.response = "Resposta do assistente mockado."
        assistant = AssistantAgent(self.mock_base_agent)
        response = assistant.get_answer("Qualquer pergunta")
        self.assertEqual(response, "Resposta do assistente mockado.")

    def test_report_agent(self):
        """
        Testa o ReportAgent com o mock do BaseAgent.
        """
        self.mock_base_agent.response = "Resumo do relatório mockado."
        data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        report_agent = ReportAgent(self.mock_base_agent, data)
        response = report_agent.generate_report("Qualquer solicitação de relatório")
        self.assertEqual(response, "Resumo do relatório mockado.")

    def test_prediction_agent(self):
        """
        Testa o PredictionAgent com o mock do BaseAgent.
        """
        self.mock_base_agent.response = "Previsão de vendas mockada."
        data = pd.DataFrame({'Mês': ['Jan'], 'Vendas': [100]})
        prediction_agent = PredictionAgent(self.mock_base_agent, data)
        response = prediction_agent.make_prediction("Qualquer solicitação de previsão")
        self.assertEqual(response, "Previsão de vendas mockada.")

if __name__ == '__main__':
    unittest.main()
