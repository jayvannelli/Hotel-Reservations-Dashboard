import streamlit as st
from src.data import df


def main():
    st.title("Room Type Analysis")

    beginning_date_selection = st.date_input(label="Starting date")
    ending_date_selection = st.date_input(label="Ending date")

    number_of_adults = st.number_input("Number of adults",
                                       min_value=df['no_of_adults'].min(),
                                       max_value=df['no_of_adults'].max())

    number_of_children = st.number_input("Number of children",
                                         min_value=df['no_of_children'].min(),
                                         max_value=df['no_of_children'].max())

    number_of_weekend_nights = st.number_input("Number of weekend nights",
                                               min_value=df['no_of_weekend_nights'].min(),
                                               max_value=df['no_of_weekend_nights'].max())

    number_of_week_nights = st.number_input("Number of week nights",
                                            min_value=df['no_of_week_nights'].min(),
                                            max_value=df['no_of_week_nights'].max())

    st.write(df)


if __name__ == "__main__":
    main()
