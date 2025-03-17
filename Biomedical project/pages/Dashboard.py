#Meditrack,Advanvced Medical Recording System
#By: Yehya Mokhtar 202400812,Laila Sobh 202400847,Ahmed Ismail 202401920,Jana Zein 202400850,Mohamed Anwar 202401921
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Meditrack")
st.write("Advanced Medical Recording System")
st.write("Welcome")
New_updated_paitent=st.button("Register or Update Paitent",type="primary")
if New_updated_paitent:
    st.switch_page("pages/Paitents.py")

doc={"Months":["Jan-Mar","April-June","July-Sep","Oct-Dec"],"values":[200,150,175,263]}

col=st.columns(5)
col[0].write("Statistics")
col[4].selectbox("category",["Num of paitents","Diagnosis"])
docdataframe=pd.DataFrame(doc)
st.bar_chart(docdataframe.set_index("Months"))

col=st.columns(2)
activity_tab=st.container(border=True)
activity_tab.write("Activity Feed")
paitent_button=activity_tab.button("Go to paitents")
activity_tab.write("You Diagnosed XYZ with ABC")
activity_tab.write("You Diagnosed XYZ with ABC")
activity_tab.write("You Diagnosed XYZ with ABC")
if paitent_button:
    st.switch_page("pages/Paitents.py")



