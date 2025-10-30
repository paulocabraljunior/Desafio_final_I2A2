# src/agents/anthropic_agent.py

from anthropic import Anthropic
from src.agents.base_agent import BaseAgent

class AnthropicAgent(BaseAgent):
    """
    Agente para interagir com a API da Anthropic.
    """

    def __init__(self, api_key):
        """
        Inicializa o agente Anthropic.
        """
        super().__init__(api_key)
        self.client = Anthropic(api_key=self.api_key)

    def generate_response(self, prompt):
        """
        Gera uma resposta usando um modelo da Anthropic.
        """
        try:
            response = self.client.messages.create(
                model="claude-2.1",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Erro ao gerar resposta da Anthropic: {e}"
