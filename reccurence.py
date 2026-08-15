def generate_occurrences(transaction, forecast_start, forecast_end):
    """Generate transaction occurrences within the forecast period."""

    occurrences = []

    if transaction.frequency == "once":
        if forecast_start <= transaction.start_date <= forecast_end:
            occurrences.append(transaction.start_date)

    return occurrences