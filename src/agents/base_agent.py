# src/agents/base_agent.py

from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Classe base abstrata para todos os agentes LLM.
    Define uma interface comum para a geração de respostas.
    """

    def __init__(self, api_key):
        """
        Inicializa o agente com a chave da API.
        :param api_key: A chave da API para o serviço LLM.
        """
        if not api_key:
            raise ValueError("A chave da API não foi fornecida.")
        self.api_key = api_key

    @abstractmethod
    def generate_response(self, prompt):
        """
        Gera uma resposta para um determinado prompt.
        Este método deve ser implementado por todas as subclasses.
        :param prompt: O prompt para enviar ao modelo LLM.
        :return: A resposta gerada pelo modelo.
        """
        pass
