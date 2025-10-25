# src/core/utils.py

"""
Funções utilitárias compartilhadas pela aplicação.
"""

import pandas as pd

def load_and_merge_data(cabecalho_path, itens_path):
    """
    Carrega os dados de cabeçalho e itens de arquivos CSV,
    e os une em um único DataFrame.

    :param cabecalho_path: Caminho para o arquivo CSV de cabeçalho.
    :param itens_path: Caminho para o arquivo CSV de itens.
    :return: DataFrame do pandas com os dados unidos.
    """
    df_cabecalho = pd.read_csv(cabecalho_path, sep=',', encoding='utf-8')
    df_itens = pd.read_csv(itens_path, sep=',', encoding='utf-8')

    # Unir os DataFrames pela chave de acesso
    df_merged = pd.merge(df_itens, df_cabecalho, on="CHAVE DE ACESSO", how="left", suffixes=('', '_dup'))

    # Remover colunas duplicadas que podem ter sido criadas com o sufixo
    df_merged.drop([col for col in df_merged.columns if '_dup' in col], axis=1, inplace=True)

    return df_merged
