import streamlit as st
import pandas as pd

file = 'AFCO Lijst.txt'
def extract_data(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if "=" in line]
    data_extracted = [line.split('=', 1) for line in filtered_lines]
    return pd.DataFrame(data_extracted, columns=['Abbreviation', 'Meaning'])

df = extract_data(file)

# Search input
search_term = st.text_input("Search abbreviation:")

if search_term:
    # Case-insensitive partial match
    filtered_df = df[df["Abbreviation"].str.contains(search_term, case=False, na=False)]

    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            meaning = row["Meaning"]
            # Google search URL
            url = f"https://www.google.com/search?q={meaning.replace(' ', '+')}"
            # Markdown link that opens in a new tab
            st.markdown(f"{row['Abbreviation']}: <a href='{url}' target='_blank'>{meaning}</a>",
                        unsafe_allow_html=True)
    else:
        st.info("No abbreviations found.")
