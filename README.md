# Cash-Flow Forecaster

Cash-Flow Forecaster is a web application that helps users plan their future cash flow by adding income and recurring expenses. The application forecasts how the user's balance changes over a selected period and identifies when the balance is expected to be at its lowest.

## Live Application

Open Cash-Flow Forecaster: (https://cashflowforecaster.streamlit.app/)

## Features

- Add income and expense transactions.
- Support one-time, weekly, monthly, and yearly transactions.
- Select a custom forecast period.
- Calculate the projected running balance.
- Display transactions in chronological order.
- Visualise the projected balance over time.
- Identify the lowest projected balance and the date on which it occurs.

## Project Structure

### `app.py`

Contains the Streamlit user interface for the application.

It allows users to:
- Enter a starting balance.
- Select the forecast start and end dates.
- Add income and expense transactions.
- Select the recurrence frequency of each transaction.
- View the transactions they have added.
- Generate a cash-flow forecast.
- View the projected balance over time.
- View the lowest projected balance and its date.

### `models.py`

Defines the `Transaction` class used to represent each income or expense transaction.

Each transaction contains:
- Name
- Amount
- Transaction type
- Frequency
- Start date

### `reccurence.py`

Handles the recurring transaction logic.

The `generate_occurrences()` function determines when each transaction occurs within the selected forecast period.

The supported frequencies are:
- One-time
- Weekly
- Monthly
- Yearly

The recurrence logic also handles differences in month lengths, including transactions that start on dates such as the 31st.

### `forecast.py`

Contains the main cash-flow forecasting logic.

It is responsible for:
- Generating forecast entries from transaction occurrences.
- Ordering transactions chronologically.
- Handling income and expense amounts.
- Calculating the running balance.
- Finding the lowest projected balance and its date.

### `tests/test_reccurence.py`

Contains unit tests for the recurrence logic, including:
- One-time transactions
- Weekly transactions
- Monthly transactions
- Monthly transactions starting on the 31st
- Yearly transactions

### `tests/test_forecast.py`

Contains unit tests for the forecasting logic, including:
- Forecast generation
- Transaction ordering
- Income and expense handling
- Running balance calculations
- Lowest balance detection

## How It Works

1. The user enters their starting balance.
2. The user selects the start and end dates of the forecast.
3. The user adds income and expense transactions.
4. Each transaction can be configured as one-time, weekly, monthly, or yearly.
5. The application generates all transaction occurrences within the selected period.
6. The occurrences are ordered chronologically.
7. Income and expenses are applied to calculate the projected running balance.
8. The application displays the cash-flow forecast and identifies the lowest projected balance.

## Running the Application Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Streamlit will display a local URL where the application can be accessed.

## Running the Tests

Run all unit tests using:

```bash
python -m unittest discover -s tests -v
```

## Technologies Used

- Python
- Streamlit
- Pandas
- Python `unittest`