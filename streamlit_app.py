import streamlit as st
import pandas as pd

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

uploaded_file = st.file_uploader("/content/FPsorted.csv", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

df.columns = df.columns.str.strip()

# Check for required columns
if "Country" in df.columns and "HDICat" in df.columns:
    countries = sorted(df["Country"].dropna().unique())

    # Create dropdown using Streamlit
    selected_country = st.selectbox("Select a country", countries)

    # Lookup the HDI Category for the selected country
    match = df[df["Country"].str.lower() == selected_country.lower()]
    
    if not match.empty:
        hdi = match.iloc[0]["HDICat"]
        st.success(f"HDI Category for **{match.iloc[0]['Country']}**: {hdi}")
    else:
        st.error("Country not found.")
else:
    st.error("Dataset must contain 'Country' and 'HDICat' columns.")
