# src/reports/report_agent.py

import pandas as pd
from src.agents.base_agent import BaseAgent

class ReportAgent:
    """
    Agente para gerar relatórios usando um agente LLM base para interpretar as solicitações.
    """

    def __init__(self, base_agent: BaseAgent, data: pd.DataFrame):
        """
        Inicializa o agente de relatórios.
        :param base_agent: Uma instância de um agente que herda de BaseAgent.
        :param data: Um DataFrame do Pandas com os dados para gerar relatórios.
        """
        self.base_agent = base_agent
        self.data = data

    def generate_report(self, user_query):
        """
        Gera um relatório com base na consulta do usuário.
        """
        prompt = f"Com base nos seguintes dados, gere um relatório conciso que responda à pergunta: '{user_query}'.\n\nDados:\n{self.data.to_string()}"

        return self.base_agent.generate_response(prompt)
