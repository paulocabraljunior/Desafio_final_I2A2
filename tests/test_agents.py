# tests/test_agents.py

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from src.agents.gemini_agent import GeminiAgent
from src.agents.openai_agent import OpenAIAgent
from src.agents.anthropic_agent import AnthropicAgent
from src.assistant.assistant_agent import AssistantAgent
from src.reports.report_agent import ReportAgent
from src.predictive_analysis.prediction_agent import PredictionAgent

class TestAgents(unittest.TestCase):
    def test_assistant_agent(self):
        mock_base_agent = MagicMock()
        mock_base_agent.generate_response.return_value = "Mocked assistant response"
        assistant_agent = AssistantAgent(mock_base_agent)
        response = assistant_agent.get_answer("test query")
        self.assertEqual(response, "Mocked assistant response")

    def test_report_agent(self):
        mock_base_agent = MagicMock()
        mock_base_agent.generate_response.return_value = "Mocked report response"
        report_agent = ReportAgent(mock_base_agent, pd.DataFrame())
        response = report_agent.generate_report("test query")
        self.assertEqual(response, "Mocked report response")

    def test_prediction_agent(self):
        mock_base_agent = MagicMock()
        mock_base_agent.generate_response.return_value = "Mocked prediction response"
        prediction_agent = PredictionAgent(mock_base_agent, pd.DataFrame())
        response = prediction_agent.make_prediction("test query")
        self.assertEqual(response, "Mocked prediction response")

if __name__ == "__main__":
    unittest.main()
