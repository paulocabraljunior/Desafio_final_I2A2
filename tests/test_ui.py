# tests/test_ui.py

import unittest
from unittest.mock import patch, MagicMock

# Mocking Streamlit components
st_mock = MagicMock()
st_mock.set_page_config = MagicMock()
st_mock.sidebar.title = MagicMock()
st_mock.sidebar.columns = MagicMock(return_value=(MagicMock(), MagicMock(), MagicMock()))
st_mock.title = MagicMock()
st_mock.selectbox = MagicMock()
st_mock.text_input = MagicMock()
st_mock.button = MagicMock()
st_mock.success = MagicMock()
st_mock.warning = MagicMock()
st_mock.session_state = MagicMock()


with patch.dict("sys.modules", {"streamlit": st_mock}):
    from src.ui import load_ui

class TestUI(unittest.TestCase):
    def setUp(self):
        st_mock.reset_mock()
        st_mock.session_state.reset_mock()

        # Configure session_state to have 'lang' = 'pt' initially
        st_mock.session_state.__contains__.side_effect = lambda key: key in ['lang', 'llm']
        st_mock.session_state.lang = 'pt'
        st_mock.session_state.llm = 'Gemini'

    def test_llm_selection(self):
        # order of button calls in load_ui: pt, en, es, save
        st_mock.button.side_effect = [False, False, False, True]
        st_mock.selectbox.return_value = "Gemini"
        st_mock.session_state.get.side_effect = ["Gemini", "test_api_key", "pt"]

        load_ui()

        st_mock.selectbox.assert_called_with(
            "Selecione o LLM:",
            ("Gemini", "OpenAI", "Anthropic")
        )

    def test_api_key_input(self):
        # order of button calls in load_ui: pt, en, es, save
        st_mock.button.side_effect = [False, False, False, True]
        st_mock.selectbox.return_value = "OpenAI"
        st_mock.session_state.get.side_effect = ["OpenAI", "test_api_key", "pt"]

        load_ui()

        st_mock.text_input.assert_called_with(
            "Chave da API de {llm}:".format(llm="OpenAI"),
            type="password"
        )

if __name__ == "__main__":
    unittest.main()
