import streamlit as st
from src.data import df


def main():
    st.title("Segment Analysis")

    df['week_night_costs'] = df['no_of_week_nights'] * df['avg_price_per_room']
    df['weekend_night_costs'] = df['no_of_weekend_nights'] * df['avg_price_per_room']
    df['total_cost'] = df['week_night_costs'] + df['weekend_night_costs']

    segment_type = st.selectbox(label="Select segment type:",
                                options=df['market_segment_type'].unique())

    segment_df = df.loc[df['market_segment_type'] == segment_type]
    st.write(segment_df)
    st.bar_chart(segment_df, x="no_of_adults", y='total_cost')


if __name__ == "__main__":
    main()
