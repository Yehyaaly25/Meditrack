#Meditrack,Advanvced Medical Recording System
#By: Yehya Mokhtar 202400812,Laila Sobh 202400847,Ahmed Ismail 202401920,Jana Zein 202400850,Mohamed Anwar 202401921
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Statistcs",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Meditrack")
st.write("Advanced Medical Recording System")
doc={"Months":["Jan-Mar","April-June","July-Sep","Oct-Dec"],"values":[200,150,175,263]}

col=st.columns(5)
col[0].write("Statistics")
col[4].selectbox("category",["Num of paitents","Diagnosis"])
docdataframe=pd.DataFrame(doc)
st.bar_chart(docdataframe.set_index("Months"))