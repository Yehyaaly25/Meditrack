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
col=st.columns(2)
paitent_first_name=col[0].text_input("First Name:")
paitent_last_name=col[1].text_input("Last Name:")
paitent_DOB=col[0].text_input("Date of Birth:")
paitent_age=col[1].number_input("Age:",step=1)
paitent_gender=st.selectbox("Gender:",["Male","Female"])
paitent_symptoms=st.text_input("Symptoms")
history_container=st.container(border=True)
history_container.write("Paitent History:")
paitent_past_meds=history_container.text_input("Past Medications:")
paitent_past_conditions=history_container.text_input("Past Conditions:")
paitent_Family_conditions=history_container.text_input("Relative Conditions:")
paitent_tests=st.text_input("Tests Done:")
paitent_diagnosis=st.text_input("Diagnosis")
