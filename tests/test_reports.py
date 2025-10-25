# tests/test_reports.py

import unittest
import pandas as pd
from src.reports.etl import DataLoader, DataTransformer
from src.reports.generator import ReportGenerator
import os

class TestReports(unittest.TestCase):
    """Testes para o módulo de relatórios."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.loader = DataLoader()
        self.transformer = DataTransformer()
        # Cria um DataFrame de exemplo para os testes.
        self.test_df = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'produto': ['A', 'B', 'A', 'C'],
            'vendas': [100, 150, 120, 80]
        })
        # Cria um arquivo CSV de teste.
        self.csv_path = 'test_data.csv'
        self.test_df.to_csv(self.csv_path, index=False)

    def tearDown(self):
        """Limpa o ambiente de teste."""
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)

    def test_load_from_csv(self):
        """Testa o carregamento de dados de um CSV."""
        df = self.loader.load_from_csv(self.csv_path)
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 4)

    def test_clean_data(self):
        """Testa a limpeza de dados."""
        df_with_duplicates = pd.concat([self.test_df, self.test_df.head(1)])
        df_cleaned = self.transformer.clean_data(df_with_duplicates)
        self.assertEqual(len(df_cleaned), 4)

    def test_report_generator_csv(self):
        """Testa a geração de relatórios em CSV."""
        generator = ReportGenerator(self.test_df)
        report_path = 'test_report.csv'
        generator.to_csv(report_path)
        self.assertTrue(os.path.exists(report_path))
        os.remove(report_path)

if __name__ == '__main__':
    unittest.main()
