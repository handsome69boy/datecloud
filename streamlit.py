import streamlit as st
import pandas as pd
from io import StringIO
from main import parse_date_with_nan

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
if uploaded_file is not None:
    # 選取欄位
    column_names = dataframe.columns.tolist()    
    selected_column = st.selectbox("選擇欄位", column_names)
    dataframe=parse_date_with_nan(dataframe,selected_column)
    st.write(dataframe)
    x=dataframe.to_csv(index=False)
    st.download_button('Download CSV',x,"hello.csv",'text/csv')

 
