"""
This file is used to generate cash-flow forecasts from transaction data.

It processes transaction occurrences, orders them by date, and calculates
the projected balance throughout the forecast period.
"""
from reccurence import generate_occurrences


def get_date(entry):
    """Return the date of a forecast entry for sorting."""
    return entry["date"]


def generate_forecast(transactions, forecast_start, forecast_end):
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