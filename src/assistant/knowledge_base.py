# src/assistant/knowledge_base.py

import json

class KnowledgeBase:
    """
    Classe para gerenciar a base de conhecimento do assistente.
    """

    def __init__(self, file_path=None):
        self.data = {}
        if file_path:
            self.load_from_json(file_path)

    def load_from_json(self, file_path):
        """Carrega a base de conhecimento de um arquivo JSON."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            print(f"Base de conhecimento carregada de {file_path}")
        except FileNotFoundError:
            print(f"Erro: Arquivo da base de conhecimento não encontrado em {file_path}")
        except json.JSONDecodeError:
            print(f"Erro: Falha ao decodificar o JSON em {file_path}")

    def get_answer(self, intent, entities):
        """
        Obtém uma resposta da base de conhecimento com base na intenção e nas entidades.
        """
        if intent in self.data:
            if not entities:
                # Se não houver entidades, retorna a resposta padrão para a intenção.
                return self.data[intent].get("default_answer", "Não encontrei uma resposta para isso.")

            # Procura uma resposta específica para as entidades.
            if "tax_type" in entities:
                tax = entities["tax_type"]
                return self.data[intent].get(tax, {}).get("description", "Não tenho informações sobre esse imposto.")

        return "Desculpe, não consegui entender a sua pergunta."

# Exemplo de um arquivo JSON para a base de conhecimento:
# {
#   "get_tax_information": {
#     "default_answer": "Sobre qual imposto você gostaria de saber?",
#     "IPI": {
#       "description": "O Imposto sobre Produtos Industrializados (IPI) é um imposto federal que incide sobre produtos industrializados."
#     },
#     "ICMS": {
#       "description": "O Imposto sobre Circulação de Mercadorias e Serviços (ICMS) é um imposto estadual."
#     }
#   }
# }
