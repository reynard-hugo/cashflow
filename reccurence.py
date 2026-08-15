from datetime import timedelta

def generate_occurrences(transaction, forecast_start, forecast_end):
    """Generate transaction occurrences within the forecast period."""

    occurrences = []

    if transaction.frequency == "once":
        if forecast_start <= transaction.start_date <= forecast_end:
            occurrences.append(transaction.start_date)
    elif transaction.frequency == "weekly":
        current_date = transaction.start_date

        while current_date <= forecast_end:
            if current_date >= forecast_start:
                occurrences.append(current_date)

            current_date += timedelta(weeks=1)


    return occurrences