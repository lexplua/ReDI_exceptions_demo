import pandas as pd
import streamlit as st

from functions.exercises import read, get_datasource, Categories, get_average_value, insert


def display_insights():
    add_insights = st.button("Show some insights")
    if add_insights:
        data = read(get_datasource())
        for category in Categories:
            st.markdown(f"Average {category} spending's: :blue[{get_average_value(category, data)}]")
        st.divider()
        chart_data = pd.read_json(get_datasource(), orient='index').groupby('category').sum()
        st.bar_chart(chart_data['amount'])


def display_records():
    st.dataframe(pd.DataFrame.from_dict(read(get_datasource()), orient='index'), use_container_width=True)


def add_expences_form():
    with st.form('Add expense', clear_on_submit=True):
        amount = st.number_input("Amount", value=0.0, help="How much you spent...")
        category = st.selectbox(
            "Category",
            options=[
                Categories.Charity.value,
                Categories.Essentials.value,
                Categories.Entertainment.value
            ]
        )
        details = st.text_input("Details", placeholder="Netflix, heating, taxes...")
        submit = st.form_submit_button("Add expense")
        if submit:
            record = {
                'amount': amount,
                'category': category,
                'details': details
            }
            insert(get_datasource(), record=record)
