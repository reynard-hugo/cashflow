"""
This file is used to generate cash-flow forecasts from transaction data.

It processes transaction occurrences, orders them by date, and calculates
the projected balance throughout the forecast period.
"""
from datetime import date

from models import Transaction
from reccurence import generate_occurrences


def get_date(entry: dict) -> date:
    """Return the date of a forecast entry for sorting."""
    return entry["date"]


def generate_forecast(transactions: list[Transaction], forecast_start: date, forecast_end: date) -> list[dict]:
    """
    Generate forecast entries for all transactions within the forecast period.
    """

    forecast = []

    for transaction in transactions:
        occurrences = generate_occurrences(
            transaction,
            forecast_start,
            forecast_end
        )

        for occurrence in occurrences:
            amount = transaction.amount

            if transaction.transaction_type == "expense":
                amount = -amount

            forecast.append({
                "date": occurrence,
                "name": transaction.name,
                "amount": amount
            })

    forecast.sort(key=get_date)

    return forecast

def calculate_balances(
    forecast: list[dict],
    starting_balance: float) -> list[dict]:    
    """
    Calculate the running balance for each forecast entry.
    """

    balance = starting_balance
    result = []

    for entry in forecast:
        balance += entry["amount"]

        result.append({
            "date": entry["date"],
            "name": entry["name"],
            "amount": entry["amount"],
            "balance": balance
        })

    return result

def find_lowest_balance(forecast: list[dict]) -> dict | None:
    """Find the lowest projected balance and its date."""

    if not forecast:
        return None

    lowest = forecast[0]

    for entry in forecast:
        if entry["balance"] < lowest["balance"]:
            lowest = entry

    return lowest