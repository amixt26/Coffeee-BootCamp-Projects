import streamlit as st
import pickle

#loading model
model = pickle.load(open('/Users/amitpandey/ml_study-2/breast_cancer_prognosis.pkl' ,'rb'))







def main():
    st.title("Breast Cancer Prognosis")

    #input variables
    radius_mean = st.number_input("Enter radius_mean")
    texture_mean = st.number_input("Enter texture_mean")

    smoothness_mean = st.number_input('Enter smoothness_mean')
    compactness_mean = st.number_input('Enter compactness_mean')

    symmetry_mean = st.number_input('Enter symmetry_mean')
    fractal_dimension_mean = st.number_input('Enter fractal_dimension_mean')
    radius_se = st.number_input('Enter radius_se')
    texture_se = st.number_input('Enter texture_se')

    smoothness_se = st.number_input('Enter smoothness_se')
    compactness_se = st.number_input('Enter compactness_se')

    concavepoints_se = st.number_input('Enter concave points_se')

    symmetry_se = st.number_input('Enter symmetry_se')

    symmetry_worst = st.number_input('Enter symmetry_worst')



    #prediction code(button)
    makeprediction = ""

    if st.button("Predict"):
     makeprediction= model.predict([[radius_mean, texture_mean, smoothness_mean, compactness_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, smoothness_se, compactness_se, concavepoints_se, symmetry_se, symmetry_worst]])
     if makeprediction == 1:
          st.success ("It's Malignant Diagnosis")

     else:
         st.success("It's Non-Maligant/Beningn Diagnosis ")
    #st.success(f' patient is {makeprediction}')





if __name__ =='__main__':
   main()

#1 ~ M = malignant, 0 ~ B = benign