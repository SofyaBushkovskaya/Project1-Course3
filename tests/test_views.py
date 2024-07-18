from unittest import TestCase, mock
import json
from src.views import web_page_home


class TestWebPageHome(TestCase):

    @mock.patch("src.views.get_read_excel")
    @mock.patch("src.views.filter_transactions_by_date")
    @mock.patch("src.views.get_cards_info")
    @mock.patch("src.views.get_exchange_rates")
    @mock.patch("src.views.get_stocks_cost")
    @mock.patch("src.views.get_top_5_transactions")
    @mock.patch("src.views.get_greeting")
    def test_web_page_home(
        self,
        mock_get_greeting,
        mock_get_top_5_transactions,
        mock_get_stocks_cost,
        mock_get_exchange_rates,
        mock_get_cards_info,
        mock_filter_transactions_by_date,
        mock_get_read_excel,
    ):
        mock_get_read_excel.return_value = []
        mock_filter_transactions_by_date.return_value = []
        mock_get_cards_info.return_value = {}
        mock_get_exchange_rates.return_value = {}
        mock_get_stocks_cost.return_value = {}
        mock_get_top_5_transactions.return_value = []
        mock_get_greeting.return_value = "Hello, world!"
        user_settings = {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "GOOGL"]}
        api_key_currency = "mock_currency_api_key"
        api_key_stocks = "mock_stocks_api_key"
        result = web_page_home("10.07.2024", user_settings, api_key_currency, api_key_stocks)
        json_result = json.loads(result)
        self.assertIn("greeting", json_result)
        self.assertEqual(json_result["greeting"], "Hello, world!")
        self.assertIn("cards", json_result)
        self.assertIn("top_transactions", json_result)
        self.assertIn("exchange_rates", json_result)
        self.assertIn("stocks", json_result)
