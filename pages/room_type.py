import streamlit as st
from src.data import df


def main():
    st.title("Room Type Analysis")

    room_type = st.selectbox(label="Select room type:",
                             options=df['room_type_reserved'].unique())

    room_type_data = df.loc[df["room_type_reserved"] == room_type]
    st.write(room_type_data)


if __name__ == "__main__":
    main()
