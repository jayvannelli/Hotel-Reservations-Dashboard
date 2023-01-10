import streamlit as st
from src.data import df


def main():
    st.title("Segment Analysis")

    segment_type = st.selectbox(label="Select segment type:",
                                options=df['market_segment_type'].unique())

    segment_df = df.loc[df['market_segment_type'] == segment_type]
    st.write(segment_df)


if __name__ == "__main__":
    main()