import streamlit as st 
import sklearn
import xgboost
import pandas as pd
import pickle

st.title("Yurak hurujini bashorat qiluvchi model")
# st.title("Quyida bemor parametrlarini kiritgan holda natijani olishingiz mumkin")

# jins = st.text_input("Jinsingizni kiriting 👇")
# yosh = st.text_input("Yoshingizni kiriting 👇")
# time = st.text_input("Necha marta yurak huruji bo'lgan? 👇")
# eject = st.text_input("Sizda Ejeksiyon fraktsiyasi qanday? 👇")
# creatinin = st.text_input("Qoningizdagi creatinin miqdorini qanday? 👇")

# natija = []
# natija.append(time)
# natija.append(eject)
# natija.append(creatinin)

# result = {"time":[natija[0], natija[0]], "ejection_fraction":[natija[1], natija[1]], "serum_creatinine":[natija[2], natija[2]]}
# df = pd.DataFrame(data=result)

# model = pickle.load(open("yurak_huruji.pkl", "rb"))
# xgb_pred = model.predict(df)
# xgb_acc = accuracy_score(y_test, xgb_pred)

# st.success(xgb_pred)

from streamlit_option_menu import option_menu


# loading the saved models

# diabetes_model = pickle.load(open('C:/Users/siddhardhan/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open("yurak_huruji.pkl", "rb"))

# parkinsons_model = pickle.load(open('C:/Users/siddhardhan/Desktop/Multiple Disease Prediction System/saved models/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu("Bir nechta kasalliklarni tekshirish",
                          
                          ['Qandli diabetga tekshirish',
                           'Yurak huruji bashorati',
                           'Parkinson kasalligi bashorati'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
# if (selected == 'Diabetes Prediction'):
    
#     # page title
#     st.title('Diabetes Prediction using ML')
    
    
#     # getting the input data from the user
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         Pregnancies = st.text_input('Number of Pregnancies')
        
#     with col2:
#         Glucose = st.text_input('Glucose Level')
    
#     with col3:
#         BloodPressure = st.text_input('Blood Pressure value')
    
#     with col1:
#         SkinThickness = st.text_input('Skin Thickness value')
    
#     with col2:
#         Insulin = st.text_input('Insulin Level')
    
#     with col3:
#         BMI = st.text_input('BMI value')
    
#     with col1:
#         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
#     with col2:
#         Age = st.text_input('Age of the Person')
    
    
#     # code for Prediction
#     diab_diagnosis = ''
    
#     # creating a button for Prediction
    
#     if st.button('Diabetes Test Result'):
#         diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
#         if (diab_prediction[0] == 1):
#           diab_diagnosis = 'The person is diabetic'
#         else:
#           diab_diagnosis = 'The person is not diabetic'
        
#     st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Yurak huruji bashorati'):
    
    # page title
    st.title('Yurak huruji bashorati')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Yosh')
        
    with col2:
        sex = st.text_input('Jins')
        
    with col3:
        cp = st.text_input('Yurak hurujlari soni')
        
    with col1:
        trestbps = st.text_input('Ejection fraktsiya')
        
    with col2:
        chol = st.text_input('Qondagi creatinin miqdori')
        
    # with col3:
    #     fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    # with col1:
    #     restecg = st.text_input('Resting Electrocardiographic results')
        
    # with col2:
    #     thalach = st.text_input('Maximum Heart Rate achieved')
        
    # with col3:
    #     exang = st.text_input('Exercise Induced Angina')
        
    # with col1:
    #     oldpeak = st.text_input('ST depression induced by exercise')
        
    # with col2:
    #     slope = st.text_input('Slope of the peak exercise ST segment')
        
    # with col3:
    #     ca = st.text_input('Major vessels colored by flourosopy')
        
    # with col1:
    #     thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Yurak huruji testi natijasi'):
        df = pd.DataFrame({"time":[int(cp), int(cp)], "ejection_fraction":[int(trestbps), int(trestbps)], "serum_creatinine":[float(chol), float(chol)]})
        heart_prediction = heart_disease_model.predict(df)                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = "Bu bemorda yurak huruji sababdan o'lim xavfi mavjud"
        else:
          heart_diagnosis = 'Bu bemorda barchasi ijobiy'
        
    st.success(heart_diagnosis)
        # st.success(df)
        
    
    

# Parkinson's Prediction Page
# if (selected == "Parkinsons Prediction"):
    
#     # page title
#     st.title("Parkinson's Disease Prediction using ML")
    
#     col1, col2, col3, col4, col5 = st.columns(5)  
    
#     with col1:
#         fo = st.text_input('MDVP:Fo(Hz)')
        
#     with col2:
#         fhi = st.text_input('MDVP:Fhi(Hz)')
        
#     with col3:
#         flo = st.text_input('MDVP:Flo(Hz)')
        
#     with col4:
#         Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
#     with col5:
#         Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
#     with col1:
#         RAP = st.text_input('MDVP:RAP')
        
#     with col2:
#         PPQ = st.text_input('MDVP:PPQ')
        
#     with col3:
#         DDP = st.text_input('Jitter:DDP')
        
#     with col4:
#         Shimmer = st.text_input('MDVP:Shimmer')
        
#     with col5:
#         Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
#     with col1:
#         APQ3 = st.text_input('Shimmer:APQ3')
        
#     with col2:
#         APQ5 = st.text_input('Shimmer:APQ5')
        
#     with col3:
#         APQ = st.text_input('MDVP:APQ')
        
#     with col4:
#         DDA = st.text_input('Shimmer:DDA')
        
#     with col5:
#         NHR = st.text_input('NHR')
        
#     with col1:
#         HNR = st.text_input('HNR')
        
#     with col2:
#         RPDE = st.text_input('RPDE')
        
#     with col3:
#         DFA = st.text_input('DFA')
        
#     with col4:
#         spread1 = st.text_input('spread1')
        
#     with col5:
#         spread2 = st.text_input('spread2')
        
#     with col1:
#         D2 = st.text_input('D2')
        
#     with col2:
#         PPE = st.text_input('PPE')
        
    
    
#     # code for Prediction
#     parkinsons_diagnosis = ''
    
#     # creating a button for Prediction    
#     if st.button("Parkinson's Test Result"):
#         parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
#         if (parkinsons_prediction[0] == 1):
#           parkinsons_diagnosis = "The person has Parkinson's disease"
#         else:
#           parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
#     st.success(parkinsons_diagnosis)
