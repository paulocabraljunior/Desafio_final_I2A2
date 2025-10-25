# Mapeamento de Fontes de Dados

Este documento mapeia as fontes de dados internas e externas para o projeto "Ferramentas Gerenciais Avançadas (Projeto Náia)".

## 1. Fontes de Dados Internas

| Fonte de Dados          | Descrição                                      | Tipo de Acesso      | Frequência de Atualização |
| ----------------------- | ---------------------------------------------- | ------------------- | ------------------------- |
| **ERP (Sistema de Gestão)** | Dados de vendas, faturamento, estoque e finanças. | Conexão com Banco de Dados | Tempo Real (Replicação)   |
| **CRM (Gestão de Clientes)** | Informações sobre clientes, leads e interações. | API REST            | Diária                     |
| **Planilhas Internas**  | Dados de planejamento orçamentário e metas.     | Upload de Arquivos  | Mensal                    |
| **Sistema de RH**       | Dados de funcionários, salários e desempenho.   | Conexão com Banco de Dados | Diária                     |

## 2. Fontes de Dados Externas

| Fonte de Dados                | Descrição                                        | Tipo de Acesso | Frequência de Atualização |
| ----------------------------- | ------------------------------------------------ | -------------- | ------------------------- |
| **IBGE (Instituto Brasileiro de Geografia e Estatística)** | Dados demográficos e econômicos do Brasil.       | API Pública    | Trimestral                |
| **Bacen (Banco Central do Brasil)** | Cotações de moedas, taxas de juros e indicadores. | API Pública    | Diária                    |
| **Fontes de Notícias do Setor** | Notícias e tendências relevantes para o mercado.  | Web Scraping   | Semanal                   |
| **Dados de Mercado (Empresas especializadas)** | Análises de concorrência e market share.         | API de Parceiros | Mensal                    |
