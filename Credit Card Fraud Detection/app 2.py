import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Loading the preprocessed dataset from the csv file using pandas

df = st.cache(pd.read_csv)('/Users/amitpandey/credit_df2.csv')
#if you set frac = .1 , then the sample() method will return 10% of the rows from the dataframe.

df = df.sample(frac=0.1,  random_state=42)

#Then it will tell us the how much out of those 10% rows are Fraud Transactions. 

#loading df
model = pickle.load(open("/Users/amitpandey/Credit_card.pkl", 'rb'))

# Print shape and description of the data
if st.sidebar.checkbox('Show what the dataframe looks like'):
    st.write(df.head(100))
    st.write('Shape of the dataframe: ', df.shape)
    st.write('Data decription: \n', df.describe())
# Print valid and fraud transactions
fraud=df[df.Class==1]
valid=df[df.Class==0]
outlier_percentage=(df.Class.value_counts()[1]/df.Class.value_counts()[0])*100
if st.sidebar.checkbox('Show fraud and valid transaction details'):
    st.write('Fraudulent transactions are: %.3f%%'%outlier_percentage)
    st.write('Fraud Cases: ',len(fraud))
    st.write('Valid Cases: ',len(valid))


