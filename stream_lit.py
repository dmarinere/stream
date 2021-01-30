import streamlit as st
import pandas as pd 
import datetime
import random
random.seed(128)


def analysis(account, age, sex, marital, amount, date):
    x = "Not Suspicious"
    if age > 18 and age < 32 : 
        if sex  == "Male": 
            if amount > 50000000: 
                x = "Suspicious"
    elif  age > 32 and age < 50:
            if amount > 10000000:
                x= "Suspicious"

    elif age > 50:
        if amount > 10000000 :
            x = "Suspicious"
    elif amount > 200000: 
       x = random.choice(["Suspicious", "Not Suspicious"])
    else:
        x = "Not Suspicious"
    return x
    
            





def main():
    st.image('./bannerlogo.jfif')
    new = st.sidebar.selectbox("Would you want details on the model or see it in Action", ["Model Description", "Model in Action"])

    if new == "Model Description":
        st.title("Suspicious Transaction Detection for Fidelity Bank Dashboard")
        st.subheader("This Dashboard would help you understand how our Suspicious Transaction model works and what component would be needed")
        st.markdown("To run our model please choose model in Action in the sidebar")
        
        st.markdown("If you are interested in finding out more about this model click the select box below\n it shows a plot of the important features and our model accuracy")
        st.markdown("\nIf you want to know more about our model performance, \nselect what you would want to know")
        sel = st.radio("Please select what you would like to know", ["None","Feature Importance", "Model Accuracy"])
        if sel == "Feature Importance":
           st.image('./features.png')
        if sel =="Model Accuracy":
            st.markdown("**Model Accuracy is 0.9980**  \n\nThe image below shows the accuracy of our model in flagging suspicious transaction, \nThe Horizontal line shows the value that was predicted and the vertical line the Actual values     \nOur model made a total of 70 wrong prediction, It labelled 61 transactions as suspicious which weren't and 9 transactions and not suspicious but they were")
            st.image('./accuracy.png')

    if new == "Model in Action":
        st.title("Suspicious Transaction Detection Model")
        st.markdown("Please enter your account number, this helps our model to uniquely identify customers")
        account = st.number_input("Input your account number", min_value=6210002922, max_value=6999999999)
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
        time = st.time_input("What time did this transaction occur")
        result = analysis(account,age, gender, marital, amount, time)
        if age != 10:
            st.markdown("**The result of your analysis is**")
            if result == "Suspicious":
                st.markdown("**Suspicious**")
            else:
                st.markdown("**Not Suspicious**")


        


if __name__ == "__main__":
    main()
