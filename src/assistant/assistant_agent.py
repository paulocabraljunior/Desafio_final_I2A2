# src/assistant/assistant_agent.py

from src.agents.base_agent import BaseAgent

class AssistantAgent:
    """
    Agente assistente que utiliza um agente LLM base para responder a perguntas.
    """

    def __init__(self, base_agent: BaseAgent):
        """
        Inicializa o agente assistente.
        :param base_agent: Uma instância de um agente que herda de BaseAgent.
        """
        self.base_agent = base_agent

    def get_answer(self, user_query):
        """
        Obtém uma resposta para a consulta do usuário usando o agente LLM base.
        """
        prompt = f"Por favor, responda à seguinte pergunta de forma clara e concisa: {user_query}"
        return self.base_agent.generate_response(prompt)
