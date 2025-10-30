# src/ui.py

import streamlit as st

def load_ui():
    """
    Carrega a interface do usuário com Streamlit.
    """
    st.set_page_config(layout="wide")

    # Dicionário de traduções
    translations = {
        "pt": {
            "title": "Configuração de Agente IA",
            "api_key_label": "Chave da API de {llm}:",
            "save_button": "Salvar Chave",
            "success_message": "Chave da API salva com sucesso!",
            "warning_message": "Por favor, insira uma chave de API válida.",
            "language_select": "Selecione o idioma:",
            "llm_select": "Selecione o LLM:"
        },
        "en": {
            "title": "AI Agent Configuration",
            "api_key_label": "{llm} API Key:",
            "save_button": "Save Key",
            "success_message": "API Key saved successfully!",
            "warning_message": "Please enter a valid API key.",
            "language_select": "Select language:",
            "llm_select": "Select LLM:"
        },
        "es": {
            "title": "Configuración del Agente de IA",
            "api_key_label": "Clave de API de {llm}:",
            "save_button": "Guardar Clave",
            "success_message": "¡Clave de API guardada con éxito!",
            "warning_message": "Por favor, ingrese una clave de API válida.",
            "language_select": "Seleccione el idioma:",
            "llm_select": "Seleccione el LLM:"
        }
    }

    # Gerenciamento de estado para idioma e LLM
    if 'lang' not in st.session_state:
        st.session_state.lang = 'pt'
    if 'llm' not in st.session_state:
        st.session_state.llm = 'Gemini'

    # Função para mudar o idioma
    def set_lang(lang_code):
        st.session_state.lang = lang_code

    # Seleção de idioma com bandeiras
    st.sidebar.title(translations[st.session_state.lang]["language_select"])
    col1, col2, col3 = st.sidebar.columns(3)
    with col1:
        if st.button("🇧🇷"):
            set_lang("pt")
    with col2:
        if st.button("🇬🇧"):
            set_lang("en")
    with col3:
        if st.button("🇪🇸"):
            set_lang("es")

    st.title(translations[st.session_state.lang]["title"])

    # Seleção do LLM
    llm_choice = st.selectbox(
        translations[st.session_state.lang]["llm_select"],
        ("Gemini", "OpenAI", "Anthropic")
    )
    st.session_state.llm = llm_choice

    # Entrada da chave da API
    api_key = st.text_input(
        translations[st.session_state.lang]["api_key_label"].format(llm=llm_choice),
        type="password"
    )

    if st.button(translations[st.session_state.lang]["save_button"]):
        if api_key:
            st.session_state.api_key = api_key
            st.success(translations[st.session_state.lang]["success_message"])
        else:
            st.warning(translations[st.session_state.lang]["warning_message"])

    return st.session_state.get("llm"), st.session_state.get("api_key"), st.session_state.lang
