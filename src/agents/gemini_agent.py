# src/agents/gemini_agent.py

import google.generativeai as genai
from src.agents.base_agent import BaseAgent

class GeminiAgent(BaseAgent):
    """
    Agente para interagir com a API do Gemini.
    """

    def __init__(self, api_key):
        """
        Inicializa o agente Gemini.
        """
        super().__init__(api_key)
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_response(self, prompt):
        """
        Gera uma resposta usando o modelo Gemini.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro ao gerar resposta do Gemini: {e}"
