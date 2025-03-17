#Meditrack,Advanvced Medical Recording System
#By: Yehya Mokhtar 202400812,Laila Sobh 202400847,Ahmed Ismail 202401920,Jana Zein 202400850,Mohamed Anwar 202401921
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Patients",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Meditrack")
st.write("Advanced Medical Recording System")

col=st.columns(3)
search_query=col[0].text_input("Search Paitents:")
new_paitent=col[1].button("New Paitent",use_container_width=True,type="primary")
if new_paitent:
    st.switch_page("pages/New_Paitent.py")
filter_box=col[2].selectbox("Sort By:",["Recents","Age"])

st.write("Recent Paitents:")

col2=st.columns(3)
recent1=col2[0].button("Yehya Mokhtar\nAge:18\nDiagnosis:Cold")
recent2=col2[1].button("Laila Sobh\nAge:18\nDiagnosis:XYZ")
recent3=col2[2].button("Ahmed Ismail\nAge:18\nDiagnosis:ABC")


st.write("All Paitents:")
col3=st.columns(3)
all0=col3[0].button("Yehya Mokhtar\nAge:18\nDiagnosis:Cold.")
all1=col3[1].button("Laila Sobh\nAge:18\nDiagnosis:XYZ.")
all2=col3[2].button("Ahmed Ismail\nAge:18\nDiagnosis:ABC.")
all0=col3[0].button("Jana Zein\nAge:18\nDiagnosis:Cold.")
all1=col3[1].button("Mohamed Anwar\nAge:18\nDiagnosis:DEF.")
all2=col3[2].button("A\nAge:18\nDiagnosis:GEH.")
all0=col3[0].button("B\nAge:18\nDiagnosis:IJK.")
all1=col3[1].button("C\nAge:18\nDiagnosis:LMN.")
all2=col3[2].button("D\nAge:18\nDiagnosis:OP.")


