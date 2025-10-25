# src/reports/etl.py

import pandas as pd

class DataLoader:
    """Classe para carregar dados de diferentes fontes."""

    def load_from_csv(self, file_path):
        """Carrega dados de um arquivo CSV."""
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Erro: Arquivo não encontrado em {file_path}")
            return None

    def load_from_database(self, connection_string, query):
        """Carrega dados de um banco de dados."""
        # A implementação da conexão com o banco de dados será adicionada aqui.
        print(f"Conectando ao banco de dados e executando a query: {query}")
        return pd.DataFrame() # Retorna um DataFrame vazio por enquanto

class DataTransformer:
    """Classe para transformar os dados carregados."""

    def clean_data(self, df):
        """Limpa os dados, removendo valores nulos e duplicados."""
        df_cleaned = df.dropna().drop_duplicates()
        return df_cleaned

    def enrich_data(self, df, external_data):
        """Enriquece os dados com informações de fontes externas."""
        # A lógica de enriquecimento de dados será implementada aqui.
        df_enriched = pd.merge(df, external_data, on='id', how='left')
        return df_enriched
