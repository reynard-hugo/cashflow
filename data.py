"""
Handles loading transaction data from JSON files.

This module reads transaction data from a JSON file and converts each
transaction into a Transaction object that can be used by the forecasting
and recurrence functions.
"""

import json
from datetime import date

from models import Transaction


def load_transactions(filename):
    """
    Load transaction data from a JSON file and convert it into Transaction objects.
    """

    with open(filename, "r") as file:
        data = json.load(file)

    transactions = []

    for item in data:
        transaction = Transaction(
            name=item["name"],
            amount=item["amount"],
            transaction_type=item["transaction_type"],
            frequency=item["frequency"],
            start_date=date.fromisoformat(item["start_date"])
        )

        transactions.append(transaction)

    return transactions