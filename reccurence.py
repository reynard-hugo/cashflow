from datetime import date, timedelta
import calendar

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

    elif transaction.frequency == "monthly":
        year = transaction.start_date.year
        month = transaction.start_date.month
        original_day = transaction.start_date.day

        while True:
            # Find the last valid day of the current month
            last_day = calendar.monthrange(year, month)[1]

            # Use the original day, or the month's last day if necessary
            day = min(original_day, last_day)

            current_date = date(year, month, day)

            if current_date > forecast_end:
                break

            if current_date >= forecast_start:
                occurrences.append(current_date)

            # Move to the next month
            month += 1

            if month > 12:
                month = 1
                year += 1
    elif transaction.frequency == "yearly":
        year = transaction.start_date.year
        original_month = transaction.start_date.month
        original_day = transaction.start_date.day

        while True:
            try:
                current_date = date(year, original_month, original_day)
            except ValueError:
                # Handle 29 February in non-leap years
                current_date = date(year, 2, 28)

            if current_date > forecast_end:
                break

            if current_date >= forecast_start:
                occurrences.append(current_date)

            year += 1
    return occurrences


def generate_forecast(transactions, forecast_start, forecast_end):
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

    return forecast