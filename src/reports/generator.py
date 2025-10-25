# src/reports/generator.py

import pandas as pd
# Para exportar para PDF, precisaremos de bibliotecas como FPDF ou ReportLab.
# Para XLSX, usaremos a integração do Pandas com o XlsxWriter.

class ReportGenerator:
    """Classe para gerar relatórios em diferentes formatos."""

    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Os dados de entrada devem ser um DataFrame do Pandas.")
        self.data = data

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
