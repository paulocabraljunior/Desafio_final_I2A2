# tests/test_assistant.py

import unittest
import json
from src.assistant.nlu import NLU
from src.assistant.knowledge_base import KnowledgeBase

class TestAssistant(unittest.TestCase):
    """Testes para o módulo do assistente."""

    def setUp(self):
        """Configura o ambiente de teste."""
        # Cria uma base de conhecimento de teste em memória.
        test_kb_data = {
            "get_tax_information": {
                "default_answer": "Sobre qual imposto você gostaria de saber?",
                "IPI": {
                    "description": "Teste: IPI é um imposto federal."
                }
            }
        }
        self.kb = KnowledgeBase()
        self.kb.data = test_kb_data
        self.nlu = NLU(self.kb)

    def test_nlu_intent_recognition(self):
        """Testa o reconhecimento de intenção do NLU."""
        intent, _ = self.nlu.parse("Qual o imposto sobre produtos?")
        self.assertEqual(intent, "get_tax_information")

    def test_nlu_entity_extraction(self):
        """Testa a extração de entidades do NLU."""
        _, entities = self.nlu.parse("Fale sobre o imposto IPI.")
        self.assertEqual(entities.get("tax_type"), "IPI")

    def test_knowledge_base_get_answer(self):
        """Testa a obtenção de respostas da base de conhecimento."""
        answer = self.kb.get_answer("get_tax_information", {"tax_type": "IPI"})
        self.assertEqual(answer, "Teste: IPI é um imposto federal.")

    def test_knowledge_base_default_answer(self):
        """Testa a resposta padrão da base de conhecimento."""
        answer = self.kb.get_answer("get_tax_information", {})
        self.assertEqual(answer, "Sobre qual imposto você gostaria de saber?")

if __name__ == '__main__':
    unittest.main()
