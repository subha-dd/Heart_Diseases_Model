import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open("trained_model2.sav" , 'rb'))

#creating a function for prediction

def diabetes_pred(input_data):

    input_data = np.asarray(input_data)

    input_data_as_np_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_np_array.reshape(1 , -1)

    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)

    if(prediction[0]==0):
        return "The Person Is Not Suffer From Heart Diseases"
    
    else:
        return "The Person Is Suffer From Heart Diseases"

    
    
def main():
    #giving a title
    st.title('Heart Diseases Prediction Model')
    
    #getting the input data from the user
    Age = st.number_input('age of a person',value=0,step=1)
    
    sex = st.number_input('Gender')
    
    cp = st.number_input('number of glucose value')
    
    trestbps= st.number_input('number of BloodPressure value')
    
    chol  = st.number_input('Cholestrol value')
    
    fbs = st.number_input('Bloodsugar value')
    
    restecg = st.number_input('ECG value')
    
    thalach = st.number_input('thalach level')
    
    exang = st.number_input('exang level')
    
    oldpeak = st.number_input('oldpeak level')
    
    slpoe = st.number_input('slope level')
    
    ca = st.number_input('ca level')
    
    thal = st.number_input('thal level')
    
    #code for prediction
    diagnosis = ''
    
    #creating a buuton for prediction
    if st.button('Heat test result'):
        diagnosis = diabetes_pred([Age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slpoe, ca, thal])
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()

