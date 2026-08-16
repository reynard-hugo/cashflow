import unittest
from datetime import date

from models import Transaction
from reccurence import generate_occurrences


class TestRecurrence(unittest.TestCase):

    def test_once_transaction(self):
        transaction = Transaction(
            "Car Service",
            300,
            "expense",
            "once",
            date(2026, 8, 15)
        )

        result = generate_occurrences(
            transaction,
            date(2026, 8, 1),
            date(2026, 8, 31)
        )

        expected = [
            date(2026, 8, 15)
        ]

        self.assertEqual(result, expected)

    def test_weekly_transaction(self):
        transaction = Transaction(
            "Groceries",
            100,
            "expense",
            "weekly",
            date(2026, 8, 1)
        )

        result = generate_occurrences(
            transaction,
            date(2026, 8, 1),
            date(2026, 8, 31)
        )

        expected = [
            date(2026, 8, 1),
            date(2026, 8, 8),
            date(2026, 8, 15),
            date(2026, 8, 22),
            date(2026, 8, 29)
        ]

        self.assertEqual(result, expected)


    def test_monthly_transaction(self):
        transaction = Transaction(
            "Rent",
            1200,
            "expense",
            "monthly",
            date(2026, 1, 5)
        )

        result = generate_occurrences(
            transaction,
            date(2026, 1, 1),
            date(2026, 3, 31)
        )

        expected = [
            date(2026, 1, 5),
            date(2026, 2, 5),
            date(2026, 3, 5)
        ]

        self.assertEqual(result, expected)

    def test_monthly_transaction_on_31st(self):
        transaction = Transaction(
            "Subscription",
            50,
            "expense",
            "monthly",
            date(2026, 1, 31)
        )

        result = generate_occurrences(
            transaction,
            date(2026, 1, 1),
            date(2026, 4, 30)
        )

        expected = [
            date(2026, 1, 31),
            date(2026, 2, 28),
            date(2026, 3, 31),
            date(2026, 4, 30)
        ]

        self.assertEqual(result, expected)

    def test_yearly_transaction(self):
        transaction = Transaction(
            "Insurance",
            500,
            "expense",
            "yearly",
            date(2026, 8, 15)
        )

        result = generate_occurrences(
            transaction,
            date(2026, 1, 1),
            date(2028, 12, 31)
        )

        expected = [
            date(2026, 8, 15),
            date(2027, 8, 15),
            date(2028, 8, 15)
        ]

        self.assertEqual(result, expected)