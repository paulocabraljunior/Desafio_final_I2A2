# tests/test_reports.py

import unittest
import pandas as pd
from src.reports.etl import DataLoader, DataTransformer
from src.reports.generator import ReportGenerator
from src.core.utils import load_and_merge_data
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

        # Create dummy files for the new test
        self.cabecalho_path = 'test_cabecalho.csv'
        self.itens_path = 'test_itens.csv'
        self.report_path = 'test_report.xlsx'


        cabecalho_df = pd.DataFrame({
            'CHAVE DE ACESSO': ['123', '456'],
            'VALOR NOTA FISCAL': [100.0, 200.0]
        })
        itens_df = pd.DataFrame({
            'CHAVE DE ACESSO': ['123', '123', '456'],
            'DESCRIÇÃO DO PRODUTO/SERVIÇO': ['PROD A', 'PROD B', 'PROD C'],
            'VALOR TOTAL': [50.0, 50.0, 200.0]
        })

        cabecalho_df.to_csv(self.cabecalho_path, index=False)
        itens_df.to_csv(self.itens_path, index=False)


    def tearDown(self):
        """Limpa o ambiente de teste."""
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
        if os.path.exists(self.cabecalho_path):
            os.remove(self.cabecalho_path)
        if os.path.exists(self.itens_path):
            os.remove(self.itens_path)
        if os.path.exists(self.report_path):
            os.remove(self.report_path)


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

    def test_load_and_merge_data(self):
        """Testa a função de carregar e mesclar dados."""
        df_merged = load_and_merge_data(self.cabecalho_path, self.itens_path)
        self.assertIsNotNone(df_merged)
        self.assertEqual(len(df_merged), 3)
        self.assertIn('VALOR NOTA FISCAL', df_merged.columns)
        self.assertIn('VALOR TOTAL', df_merged.columns)

    def test_generator_with_loaded_data(self):
        """Testa a geração de relatório com dados carregados."""
        generator = ReportGenerator()
        generator.load_data_from_zip_files(self.cabecalho_path, self.itens_path)
        generator.to_xlsx(self.report_path)
        self.assertTrue(os.path.exists(self.report_path))


if __name__ == '__main__':
    unittest.main()
