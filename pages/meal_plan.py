import streamlit as st
from src.data import df


def main():
    st.title("Meal Plan Analysis")

    meal_plan = st.selectbox(label="Select meal plan:",
                             options=df['type_of_meal_plan'].unique())

    meal_plan_data = df.loc[df["type_of_meal_plan"] == meal_plan]
    st.write(meal_plan_data)


if __name__ == "__main__":
    main()
