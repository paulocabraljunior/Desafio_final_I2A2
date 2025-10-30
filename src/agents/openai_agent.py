# src/agents/openai_agent.py

from openai import OpenAI
from src.agents.base_agent import BaseAgent

class OpenAIAgent(BaseAgent):
    """
    Agente para interagir com a API da OpenAI.
    """

    def __init__(self, api_key):
        """
        Inicializa o agente OpenAI.
        """
        super().__init__(api_key)
        self.client = OpenAI(api_key=self.api_key)

    def generate_response(self, prompt):
        """
        Gera uma resposta usando um modelo da OpenAI.
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao gerar resposta da OpenAI: {e}"
