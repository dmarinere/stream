import streamlit as st
import pandas as pd 



def analysis(account, age, sex, marital, amount, date, status):
    pass




def main():
    st.image('./bannerlogo.jfif', caption="We keep our word")
    st.title("Fraud Detection for Fidelity Bank Dashboard")
    st.subheader("This Dashboard would help you understand how our fraud detection model works and what component would be needed")
        
    new = st.sidebar.selectbox("Would you want details on the model or see it in Action", ["Model Description", "Model in Action"])
    if new == "Model Description": 
        st.subheader('The inputs for this Model is the Account Number, Age, Sex, Marital Status, Transaction Amount, Date, Bank Account Status')
        st.text("    ")
        st.text("Please enter the account number, our model uses this to uniquely identify users")
        account =st.number_input("Account number details please must be 10 digit", min_value=1000000000, max_value=9999999999)

        st.text("Please enter your age, our model uses this value to predict ")
        st.text("how likely you are to engage in this")
        age = st.number_input("Age range is from 10 to 90", min_value=10, max_value=90)
        st.text("Please enter your gender")
        gender =st.selectbox("What is your gender?", ["Male", "Female"])
        st.text("Please select your marital Status")
        marital = st.selectbox("What is your marital Status", ["Single", "Divorced", "Married"])
        st.text("Please input transaction amount, The model use this value and previous values")
        st.text("already in the model for the account")
        amount = st.number_input("What is the credit alert amount")

        


if __name__ == "__main__":
    main()