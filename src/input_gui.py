import streamlit as st
import pandas as pd
from pdf_gen import generator
from sync_local import syncing
import time

# Load data from CSV
df = pd.read_csv("utils/data.csv")

# Get unique values for dropdowns
primary_categories = df["Primary Category"].unique().tolist()
secondary_categories = df["Secondary Category"].unique().tolist()
brands = df["Brand"].unique().tolist()

def clear_text(): # this is the function you define (def is a Python keyword and is short for 'define')
  st.session_state["primary_category"] = ''  # add "text" as a key using the square brackets notation and set it to have the value ''
  st.session_state["secondary_category"] = ''  # add "text" as a key using the square brackets notation and set it to have the value ''
  st.session_state["brand"] = ''  # add "text" as a key using the square brackets notation and set it to have the value ''

def main():
    # Initialize session state for input values
    if 'reset_inputs' not in st.session_state:
        st.session_state.reset_inputs = False

    st.title("Catalogue Generator")

    # Dropdowns for user input
    if st.session_state.reset_inputs:
        primary_category = st.selectbox("Primary Category", [""] + primary_categories, key="primary_category", index=0)
        secondary_category = st.selectbox("Secondary Category", [""] + secondary_categories, key="secondary_category", index=0)
        brand = st.selectbox("Brand", [""] + brands, key="brand", index=0)
        st.session_state.reset_inputs = False
    else:
        primary_category = st.selectbox("Primary Category", [""] + primary_categories, key="primary_category")
        secondary_category = st.selectbox("Secondary Category", [""] + secondary_categories, key="secondary_category")
        brand = st.selectbox("Brand", [""] + brands, key="brand")

    # Buttons for generating PDF and syncing data
    if st.button("Generate PDF"):
        with st.spinner('Generating PDF...'):
            generator(primary_category, secondary_category, brand)
            st.success("PDF generated successfully and email sent!")
            time.sleep(5)
            st.rerun()

    if st.button("Sync Data"):
        with st.spinner('Syncing data...'):
            syncing()
            st.success("Data synced successfully!")
            time.sleep(5)
            st.rerun()

    st.button("Create New Entry", on_click=clear_text)

if __name__ == "__main__":
    main()