import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Streamlit Widgets ")

name = st.text_input("Enter your name: ")
st.write(f"Hello {name}")

age = st.slider("Enter your age: ", 0,100,18)
st.write(f"Age: {age}")

options = ['Python', 'CPP', 'Java', 'C', 'JavaScript']
choice = st.selectbox("Choose your favourite language: ", options)
st.write(f"Favourite language: {choice}")

uploaded_file = st.file_uploader("Enter your CSV file: ", type="csv")

@st.cache_data
def load_data(file):
    file.seek(0)
    return pd.read_csv(file)

if uploaded_file is not None:
    with st.spinner("Loading data..."):
        df = load_data(uploaded_file)

    st.success("Data loaded!")
    st.dataframe(df.head(20))
    
    ##Plotting code: 
    plot_df = (
    df["job_title"]
      .value_counts()
      .head(10)
      .reset_index()
    )
    plot_df.columns = ["job_title", "count"]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        data=plot_df,
        x="job_title",
        y="count",
        ax=ax
    )
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

    

