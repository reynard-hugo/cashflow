"""
This file is used to define the data model for the Cash-Flow Forecaster.

It contains the Transaction class, which represents an income or expense
transaction and stores its details.
"""
from datetime import date

class Transaction:
    """Represents an income or expense transaction in the cash-flow forecast."""
    def __init__(
        self,
        name: str,
        amount: float,
        transaction_type: str,
        frequency: str,
        start_date: date
    ) -> None:
        self.name = name
        self.amount = amount
        self.transaction_type = transaction_type
        self.frequency = frequency
        self.start_date = start_date