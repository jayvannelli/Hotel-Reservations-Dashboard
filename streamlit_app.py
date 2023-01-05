import streamlit as st
import pandas as pd


def get_data() -> pd.DataFrame:
    """Return hotel reservation CSV data as pandas DataFrame."""
    _df = pd.read_csv("data/Hotel_Reservations.csv")
    return _df


def main():
    st.title("Hotel Reservations Dashboard")

    df = get_data()
    st.write(df)


if __name__ == "__main__":
    main()
