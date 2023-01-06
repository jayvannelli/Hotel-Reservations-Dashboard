import streamlit as st
from src.data import df


def main():
    st.title("Hotel Reservations Dashboard")

    st.write(df)


if __name__ == "__main__":
    main()
