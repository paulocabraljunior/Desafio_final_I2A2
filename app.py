# app.py

import streamlit as st
from src.ui import load_ui
from src.assistant.assistant_agent import AssistantAgent
from src.reports.report_agent import ReportAgent
from src.predictive_analysis.prediction_agent import PredictionAgent
from src.agents.gemini_agent import GeminiAgent
from src.agents.openai_agent import OpenAIAgent
from src.agents.anthropic_agent import AnthropicAgent
import pandas as pd

def get_agent(llm, api_key):
    """
    Cria uma instância do agente LLM apropriado.
    """
    if llm == "Gemini":
        return GeminiAgent(api_key=api_key)
    elif llm == "OpenAI":
        return OpenAIAgent(api_key=api_key)
    elif llm == "Anthropic":
        return AnthropicAgent(api_key=api_key)
    else:
        st.error("LLM selecionado inválido.")
        return None

def main():
    """
    Função principal para rodar a aplicação Streamlit.
    """
    llm, api_key, lang = load_ui()

    if api_key:
        st.sidebar.success("API Key configurada!")

        # Dicionário de traduções e outras configurações
        translations = {
            "pt": {"welcome": "Bem-vindo...", "select_agent": "Selecione um agente:", "assistant": "Assistente", "reports": "Relatórios", "predictions": "Previsões", "query": "Sua pergunta:", "submit": "Enviar", "response": "Resposta:", "upload": "Carregue um CSV"},
            "en": {"welcome": "Welcome...", "select_agent": "Select an agent:", "assistant": "Assistant", "reports": "Reports", "predictions": "Predictions", "query": "Your question:", "submit": "Submit", "response": "Response:", "upload": "Upload a CSV"},
            "es": {"welcome": "Bienvenido...", "select_agent": "Seleccione un agente:", "assistant": "Asistente", "reports": "Informes", "predictions": "Predicciones", "query": "Su pregunta:", "submit": "Enviar", "response": "Respuesta:", "upload": "Subir un CSV"}
        }

        st.header(translations[lang]["welcome"])

        agent_choice = st.selectbox(
            translations[lang]["select_agent"],
            (translations[lang]["assistant"], translations[lang]["reports"], translations[lang]["predictions"])
        )

        uploaded_file = None
        if agent_choice != translations[lang]["assistant"]:
            uploaded_file = st.file_uploader(translations[lang]["upload"], type="csv")

        user_query = st.text_area(translations[lang]["query"])

        if st.button(translations[lang]["submit"]):
            if user_query:
                base_agent = get_agent(llm, api_key)
                if base_agent:
                    response = ""
                    if agent_choice == translations[lang]["assistant"]:
                        specialized_agent = AssistantAgent(base_agent)
                        response = specialized_agent.get_answer(user_query)

                    elif uploaded_file:
                        data = pd.read_csv(uploaded_file)
                        if agent_choice == translations[lang]["reports"]:
                            specialized_agent = ReportAgent(base_agent, data)
                            response = specialized_agent.generate_report(user_query)
                        elif agent_choice == translations[lang]["predictions"]:
                            specialized_agent = PredictionAgent(base_agent, data)
                            response = specialized_agent.make_prediction(user_query)
                    else:
                        st.warning("Por favor, carregue um arquivo de dados.")

                    st.subheader(translations[lang]["response"])
                    st.write(response)
            else:
                st.warning("Por favor, insira uma pergunta.")

if __name__ == "__main__":
    main()
