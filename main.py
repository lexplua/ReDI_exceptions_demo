import streamlit as st

from web.interface import display_insights, display_records, add_expences_form


def main():
    add_expences_form()
    st.divider()
    display_records()
    st.divider()
    display_insights()


if __name__ == "__main__":
    main()

