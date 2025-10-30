# src/reports/generator.py

import pandas as pd
from src.core.utils import load_and_merge_data
# Para exportar para PDF, precisaremos de bibliotecas como FPDF ou ReportLab.
# Para XLSX, usaremos a integração do Pandas com o XlsxWriter.

class ReportGenerator:
    """Classe para gerar relatórios em diferentes formatos."""

    def __init__(self, data=None):
        if data is not None and not isinstance(data, pd.DataFrame):
            raise TypeError("Os dados de entrada devem ser um DataFrame do Pandas.")
        self.data = data

    def load_data_from_zip_files(self, cabecalho_path, itens_path):
        """Carrega e mescla os dados dos arquivos CSV."""
        self.data = load_and_merge_data(cabecalho_path, itens_path)

    def to_csv(self, file_path):
        """Gera um relatório em formato CSV."""
        try:
            self.data.to_csv(file_path, index=False)
            print(f"Relatório gerado com sucesso em {file_path}")
        except Exception as e:
            print(f"Erro ao gerar o relatório CSV: {e}")

    def to_xlsx(self, file_path):
        """Gera um relatório em formato XLSX."""
        try:
            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                self.data.to_excel(writer, index=False, sheet_name='Relatorio')
            print(f"Relatório gerado com sucesso em {file_path}")
        except Exception as e:
            print(f"Erro ao gerar o relatório XLSX: {e}")

    def to_pdf(self, file_path):
        """Gera um relatório em formato PDF."""
        # A implementação da geração de PDF será adicionada aqui.
        print(f"Gerando relatório em PDF em {file_path}...")
        print("Funcionalidade de exportação para PDF a ser implementada.")

if __name__ == '__main__':
    # Criar uma instância do gerador de relatórios
    report_generator = ReportGenerator()

    # Carregar os dados dos arquivos extraídos
    cabecalho_path = 'unzipped_data/202401_NFs_Cabecalho.csv'
    itens_path = 'unzipped_data/202401_NFs_Itens.csv'
    report_generator.load_data_from_zip_files(cabecalho_path, itens_path)

    # Gerar um relatório em formato XLSX
    report_generator.to_xlsx('relatorio_final.xlsx')
