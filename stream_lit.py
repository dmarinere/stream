import streamlit as st
import pandas as pd 
import datetime



def analysis(account, age, sex, marital, amount, date, status):
    pass




def main():
    st.image('./bannerlogo.jfif', caption="We keep our word")
    st.title("Fraud Detection for Fidelity Bank Dashboard")
    st.subheader("This Dashboard would help you understand how our fraud detection model works and what component would be needed")
        
    new = st.sidebar.selectbox("Would you want details on the model or see it in Action", ["Model Description", "Model in Action"])
    if new == "Model in Action":
        st.markdown("Please enter your age, our model uses this value to predict \nhow likely you are to engage in this")
        age = st.number_input("Age range is from 10 to 90", min_value=10, max_value=90)
        st.markdown("Please enter your gender")
        gender =st.selectbox("What is your gender?", ["Male", "Female"])
        st.markdown("Please select your marital Status")
        marital = st.selectbox("What is your marital Status", ["Single", "Divorced", "Married"])
        st.markdown("Please input transaction amount, The model use this value and previous value \nalready in the database for the account")
        amount = st.number_input("What is the transaction amount")
        st.markdown("Please input the day and time of this transaction")
        st.date_input("What day did this transaction occur")
        st.time_input("What time did this transaction occur")


        


if __name__ == "__main__":
    main()
