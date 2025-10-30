# src/assistant/nlu.py

class NLU:
    """
    Classe para processamento de linguagem natural (NLU).
    Esta é uma implementação simples baseada em palavras-chave.
    """

    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def parse(self, user_query):
        """
        Analisa a consulta do usuário para extrair a intenção e as entidades.
        """
        query = user_query.lower()
        intent = self._identify_intent(query)
        entities = self._extract_entities(query, intent)
        return intent, entities

    def _identify_intent(self, query):
        """Identifica a intenção do usuário."""
        if "relatório de vendas" in query:
            return "get_sales_report"
        if "previsão de faturamento" in query:
            return "get_revenue_forecast"
        if "imposto" in query or "tributo" in query:
            return "get_tax_information"
        return "unknown"

    def _extract_entities(self, query, intent):
        """Extrai entidades da consulta."""
        entities = {}
        if intent == "get_tax_information":
            # Exemplo simples de extração de entidade.
            if "ipi" in query:
                entities["tax_type"] = "IPI"
            if "icms" in query:
                entities["tax_type"] = "ICMS"
        return entities
