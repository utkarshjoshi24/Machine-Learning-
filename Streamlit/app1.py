import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit App")

st.write("This is my first streamlit app")

df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

st.write("DataFrame: ")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randint(0, 20, size=(20, 3)),
    columns=['a', 'b', 'c']
)

st.write("Chart: ")
st.line_chart(chart_data) 