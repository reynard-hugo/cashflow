"""
This file is used to provide the Streamlit user interface for the
Cash-Flow Forecaster.

It allows users to add income and expense transactions, select a forecast
period, and view their projected balance and lowest balance.
"""
import streamlit as st
import pandas as pd
from datetime import date

from models import Transaction
from forecast import (
    generate_forecast,
    calculate_balances,
    find_lowest_balance
)


st.title("Cash-Flow Forecaster")
st.write(
    "Plan your future cash flow by adding income and recurring expenses. "
    "The app forecasts your balance over time and identifies when your "
    "balance is expected to be at its lowest."
)
# Store transactions during the current Streamlit session
if "transactions" not in st.session_state:
    st.session_state.transactions = []


# Forecast Settings

st.subheader("Forecast Settings")

starting_balance = st.number_input(
    "Starting Balance",
    min_value=0.0,
    value=1000.0
)

forecast_start = st.date_input(
    "Forecast Start",
    value=date.today()
)

forecast_end = st.date_input(
    "Forecast End",
    value=date.today()
)


# Add Transaction

st.subheader("Add Transaction")

with st.form("transaction_form", clear_on_submit=True):

    name = st.text_input(
        "Transaction Name"
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        value=0.0
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["income", "expense"]
    )

    frequency = st.selectbox(
        "Frequency",
        ["once", "weekly", "monthly", "yearly"]
    )

    transaction_start_date = st.date_input(
        "Transaction Start Date",
        value=date.today()
    )

    add_transaction = st.form_submit_button(
        "Add Transaction"
    )


if add_transaction:

    if name == "":
        st.error("Please enter a transaction name.")

    elif amount <= 0:
        st.error("Amount must be greater than zero.")

    else:
        transaction = Transaction(
            name,
            amount,
            transaction_type,
            frequency,
            transaction_start_date
        )

        st.session_state.transactions.append(
            transaction
        )

        st.success(
            "Transaction added successfully."
        )


# Transaction List

st.subheader("Your Transactions")

if len(st.session_state.transactions) == 0:
    st.write("No transactions added yet.")

else:
    transaction_data = []

    for transaction in st.session_state.transactions:

        transaction_data.append({
            "Name": transaction.name,
            "Amount": transaction.amount,
            "Type": transaction.transaction_type,
            "Frequency": transaction.frequency,
            "Start Date": transaction.start_date
        })

    transaction_df = pd.DataFrame(transaction_data)

    st.dataframe(
        transaction_df,
        use_container_width=True
    )


# Generate Forecast

st.subheader("Cash-Flow Forecast")

if st.button("Generate Forecast"):

    if forecast_end < forecast_start:
        st.error(
            "Forecast end date must be after the forecast start date."
        )

    elif len(st.session_state.transactions) == 0:
        st.error(
            "Please add at least one transaction."
        )

    else:
        forecast = generate_forecast(
            st.session_state.transactions,
            forecast_start,
            forecast_end
        )

        balances = calculate_balances(
            forecast,
            starting_balance
        )

        lowest = find_lowest_balance(
            balances
        )

        if len(balances) == 0:
            st.warning(
                "No transactions occur within the selected forecast period."
            )

        else:
            # Forecast Table

            forecast_data = []

            for entry in balances:
                forecast_data.append({
                    "Date": entry["date"],
                    "Transaction": entry["name"],
                    "Amount": entry["amount"],
                    "Balance": entry["balance"]
                })

            forecast_df = pd.DataFrame(
                forecast_data
            )

            st.write("### Forecast Details")

            st.dataframe(
                forecast_df,
                use_container_width=True
            )

            # Forecast Chart

            st.write("### Projected Balance")

            chart_data = forecast_df[
                ["Date", "Balance"]
            ].copy()

            chart_data = chart_data.set_index(
                "Date"
            )

            st.line_chart(
                chart_data
            )

            # Lowest Balance

            if lowest is not None:

                st.write(
                    "### Lowest Projected Balance"
                )

                st.metric(
                    "Lowest Balance",
                    f"RM {lowest['balance']:.2f}"
                )

                st.write(
                    "Date:",
                    lowest["date"]
                )