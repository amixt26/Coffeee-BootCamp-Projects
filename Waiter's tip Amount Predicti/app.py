import streamlit as st
import pickle


#loading model
model = pickle.load(open('/Users/amitpandey/ml_study-2/tip_amount_prediction.pkl', 'rb'))

def main():
    st.title("Waiter's Tip Amount Prediction")


    #input variables

    total_bill = st.number_input("Type your Total Bill Here")
    size = st.selectbox('Enter the size of people who showed up at table ', [0, 1, 2, 3, 4, 5, 6])
    st.header('The waiter was male or female')
    Female = st.selectbox('If the sex/gender is Female then select 1 else 0', [1, 0])
    Male = st.selectbox('If the sex/gender is Male then select 1 else 0', [1, 0])
    st.header('The waiter was smoker or not')
    No = st.selectbox('If the waiter is not a smoker select 1 or else 0', [1, 0])
    Yes = st.selectbox('If the waiter is a smoker select 1 or else 0', [1, 0])
    st.header("What was the day when the waiter attended customer")
    Fri = st.selectbox('If It was Friday select 1 or else 0', [1, 0])
    Sat = st.selectbox('If It was Saturday select 1 or else 0', [1, 0])
    Sun = st.selectbox('If It was Sunday select 1 or else 0', [1, 0])
    Thur = st.selectbox('If It was Thursday select 1 or else 0', [1, 0])
    st.header("What was the time when customer showed up at the table ")
    Dinner = st.selectbox('If It was Dinner time select 1 or else 0 ', [1, 0])
    Lunch = st.selectbox('If It was Lunch time select 1 or else 0 ', [1, 0])

    #prediction code(buttons)
    makeprediction = ""


    if st.button('Predict'):
        makeprediction = model.predict([[total_bill, size, Female, Male, No, Yes, Fri, Sat, Sun, Thur, Dinner, Lunch]])
    st.success(f"The Waiter's tip might be : $ {makeprediction}")

if __name__ == '__main__':
    main()

