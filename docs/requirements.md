# Requisitos Funcionais e Não Funcionais

Este documento detalha os requisitos funcionais e não funcionais para o projeto "Ferramentas Gerenciais Avançadas (Projeto Náia)".

## 1. Requisitos Funcionais

### Módulo de Relatórios Personalizados
*   **RF001:** O sistema deve permitir que os usuários criem relatórios personalizados selecionando métricas e dimensões de diferentes fontes de dados.
*   **RF002:** O sistema deve permitir a exportação de relatórios nos formatos PDF, XLSX e CSV.
*   **RF003:** O sistema deve permitir o agendamento da geração e envio de relatórios por e-mail.
*   **RF004:** Os relatórios devem ser visualizados em dashboards interativos.

### Módulo de Análises Preditivas
*   **RF005:** O sistema deve fornecer modelos de machine learning para prever tendências de vendas, churn de clientes e demanda de estoque.
*   **RF006:** O sistema deve permitir que os usuários simulem cenários de negócios ajustando variáveis como preço, investimento em marketing e custos operacionais.
*   **RF007:** Os resultados das simulações devem ser apresentados em gráficos e tabelas comparativas.

### Módulo Assistente Consultor
*   **RF008:** O assistente deve responder a perguntas em linguagem natural sobre tópicos contábeis, fiscais e políticas internas.
*   **RF009:** O assistente deve ser capaz de buscar informações nos relatórios e dados do sistema para fornecer respostas contextuais.
*   **RF010:** A base de conhecimento do assistente deve ser atualizável para refletir mudanças na legislação e nas políticas da empresa.

## 2. Requisitos Não Funcionais

*   **RNF001 (Performance):** O sistema deve carregar dashboards e relatórios em menos de 5 segundos. As consultas complexas não devem exceder 30 segundos.
*   **RNF002 (Segurança):** O acesso aos dados deve ser controlado por níveis de permissão (RBAC - Role-Based Access Control). Todos os dados sensíveis devem ser criptografados em trânsito e em repouso.
*   **RNF003 (Usabilidade):** A interface do usuário deve ser intuitiva e seguir os princípios de design de UX, minimizando a curva de aprendizado.
*   **RNF004 (Escalabilidade):** A arquitetura do sistema deve ser capaz de suportar um aumento de 50% no volume de dados e no número de usuários em um ano sem degradação significativa da performance.
*   **RNF005 (Disponibilidade):** O sistema deve ter uma disponibilidade de 99.5%.
