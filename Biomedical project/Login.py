#Meditrack,Advanvced Medical Recording System
#By: Yehya Mokhtar 202400812,Laila Sobh 202400847,Ahmed Ismail 202401920,Jana Zein 202400850,Mohamed Anwar 202401921
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Login",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Meditrack")
st.write("Advanced Medical Recording System")
option=st.selectbox("Login or Sign up",["Login","Sign Up"])
if option=="Login":
    username=st.text_input("Enter Username: ")
    password=st.text_input("Enter Password: ",type="password")
    Login_button=st.button("Login",type="primary")
    
    if Login_button==True:
        f=open("Usernames & Passwords.txt","r")
        for i in f:
            system_user=i.split(":")[0]
            system_password=i.split(":")[1]
            if username==system_user and password==system_password:
                st.success("Login sucessful.")
                st.switch_page("pages/Dashboard.py")
                f.close()
                break;
        else:
            st.exception("Incorrect username or password")

if option=="Sign Up":
    username=st.text_input("Set Username: ")
    password=st.text_input("Set Password: ",type="password")
    create_account_button=st.button("Create Account",type="primary")
    if create_account_button==True:
        f=open("Usernames & Passwords.txt","a")
        f.write(f"{username}:{password}")
        f.close()
        st.switch_page("pages/Dashboard.py")






