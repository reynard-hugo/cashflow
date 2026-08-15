class Transaction:
    """Represents an income or expense transaction in the cash-flow forecast."""
    def __init__(self, name, amount, transaction_type, frequency, start_date):
        self.name = name
        self.amount = amount
        self.transaction_type = transaction_type
        self.frequency = frequency
        self.start_date = start_date