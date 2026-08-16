import unittest
from datetime import date

from models import Transaction
from forecast import (
    generate_forecast,
    calculate_balances,
    find_lowest_balance
)


class TestForecast(unittest.TestCase):

    def test_generate_forecast(self):
        transactions = [
            Transaction(
                "Rent",
                1200,
                "expense",
                "once",
                date(2026, 8, 3)
            ),
            Transaction(
                "Salary",
                3000,
                "income",
                "once",
                date(2026, 8, 1)
            )
        ]

        result = generate_forecast(
            transactions,
            date(2026, 8, 1),
            date(2026, 8, 31)
        )

        # Check transactions are sorted by date
        self.assertEqual(result[0]["name"], "Salary")
        self.assertEqual(result[1]["name"], "Rent")

        # Check income is positive and expense is negative
        self.assertEqual(result[0]["amount"], 3000)
        self.assertEqual(result[1]["amount"], -1200)


    def test_calculate_balances(self):
        forecast = [
            {
                "date": date(2026, 8, 1),
                "name": "Salary",
                "amount": 3000
            },
            {
                "date": date(2026, 8, 3),
                "name": "Rent",
                "amount": -1200
            }
        ]

        result = calculate_balances(
            forecast,
            2000
        )

        self.assertEqual(result[0]["balance"], 5000)
        self.assertEqual(result[1]["balance"], 3800)


    def test_find_lowest_balance(self):
        forecast = [
            {
                "date": date(2026, 8, 1),
                "name": "Salary",
                "amount": 3000,
                "balance": 5000
            },
            {
                "date": date(2026, 8, 3),
                "name": "Rent",
                "amount": -1200,
                "balance": 3800
            },
            {
                "date": date(2026, 8, 5),
                "name": "Groceries",
                "amount": -500,
                "balance": 3300
            }
        ]

        result = find_lowest_balance(forecast)

        self.assertEqual(result["balance"], 3300)
        self.assertEqual(result["date"], date(2026, 8, 5))
