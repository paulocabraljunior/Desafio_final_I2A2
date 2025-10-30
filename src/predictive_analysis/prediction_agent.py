# src/predictive_analysis/prediction_agent.py

import pandas as pd
from src.agents.base_agent import BaseAgent

class PredictionAgent:
    """
    Agente para fazer previsões usando um agente LLM base.
    """

    def __init__(self, base_agent: BaseAgent, data: pd.DataFrame):
        """
        Inicializa o agente de previsão.
        :param base_agent: Uma instância de um agente que herda de BaseAgent.
        :param data: Um DataFrame do Pandas com os dados históricos.
        """
        self.base_agent = base_agent
        self.data = data

    def make_prediction(self, user_query):
        """
        Faz uma previsão com base na consulta do usuário.
        """
        prompt = f"Com base nos seguintes dados históricos, faça uma previsão detalhada que responda à pergunta: '{user_query}'.\n\nDados:\n{self.data.to_string()}"

        return self.base_agent.generate_response(prompt)
