import streamlit as st
import pickle


#loading model
model = pickle.load(open('/Users/amitpandey/ml_study-2/House_price_detect.pkl', 'rb'))

def main():
    st.title('House Prediction Model')


    #input variables
    SqFt = st.slider("Enter SqFt of the house", 1, 10000, 1)

    Bedrooms = st.selectbox('Enter no of Bedrooms', [0, 1, 2, 3, 4, 5])

    Bathrooms = st.selectbox('Enter no of Bathrooms', [0, 2, 3, 4])

    Offers = st.selectbox('Any Offers', [0, 1, 2, 3, 4, 5, 6])

    st.header('Does the house has any brick')

    No = st.selectbox('If there is no brick, then select 1 or in any other case select 0', [1,0])

    Yes = st.selectbox('If there is brick , then select 1 or in any other case select 0 ', [1,0])

    st.header('In which directions are Neighbor East, North, West')

    East = st.selectbox('neighbor in East yes=1,or no=0', [1, 0])

    North = st.selectbox('neighbor in North yes=1, or no=0', [1, 0])

    West = st.selectbox('West in neighbor yes=1, or no=0', [1, 0])



    #prediction code(buttons)
    makeprediction = ""


    if st.button('Predict'):
        makeprediction = model.predict([[SqFt, Bedrooms, Bathrooms,Offers, No, Yes, East, North, West]])
    st.success(f'The house price is : $ {makeprediction}')

if __name__ == '__main__':
    main()

