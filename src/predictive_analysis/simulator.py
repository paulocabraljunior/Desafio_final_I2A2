# src/predictive_analysis/simulator.py

import pandas as pd

class ScenarioSimulator:
    """Classe para simular cenários de negócios."""

    def __init__(self, model, base_data):
        self.model = model
        if not isinstance(base_data, pd.DataFrame):
            raise TypeError("Os dados de base devem ser um DataFrame do Pandas.")
        self.base_data = base_data

    def run_simulation(self, variable, percentage_change):
        """
        Executa uma simulação alterando uma variável específica.

        :param variable: A variável a ser alterada (ex: 'preco').
        :param percentage_change: A mudança percentual a ser aplicada (ex: 0.1 para 10% de aumento).
        :return: O resultado da simulação.
        """
        if variable not in self.base_data.columns:
            raise ValueError(f"A variável '{variable}' não foi encontrada nos dados de base.")

        simulated_data = self.base_data.copy()
        simulated_data[variable] *= (1 + percentage_change)

        # Assume que as colunas restantes são as features para o modelo.
        features = simulated_data.drop('vendas', axis=1, errors='ignore')

        # Faz a predição com os dados simulados.
        predicted_sales = self.model.predict(features)

        # Calcula o impacto da mudança.
        original_sales = self.base_data['vendas'].sum()
        simulated_sales_sum = predicted_sales.sum()
        impact = simulated_sales_sum - original_sales

        print(f"Simulação concluída: Mudança de {percentage_change:.2%} em '{variable}'")
        print(f"Vendas originais: {original_sales:.2f}")
        print(f"Vendas simuladas: {simulated_sales_sum:.2f}")
        print(f"Impacto estimado: {impact:.2f}")

        return {
            'variable': variable,
            'percentage_change': percentage_change,
            'original_sales': original_sales,
            'simulated_sales': simulated_sales_sum,
            'impact': impact
        }
