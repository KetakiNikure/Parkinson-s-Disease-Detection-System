# KNN ALGO
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit.components.v1 import html

# import pyautogui

# loading the saved models

parkinsons_model = pickle.load(open('parkinsons_detection_model.sav', 'rb'))
# print(parkinsons_model)


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Parkinsons Disease Detection',
                          ['About', 'Parkinsons Test', 'Accuracy'],
                          icons=['person','pen','check2-circle'],
                          default_index=0)
    

# Parkinson's Prediction 
if (selected == "Accuracy"):
    st.title("Accuracy ")
    st.header("89.9%")
    
    
if (selected == "About"):

   
    st.title("Parkinson's Disease ")
    st.write("Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.")
    
    img1 = Image.open("images.jpg")
   
    
    st.write("In the early stages of Parkinson's disease, your face may show little or no expression. Your arms may not swing when you walk. Your speech may become soft or slurred. Parkinson's disease symptoms worsen as your condition progresses over time.")
    st.write("Although Parkinson's disease can't be cured, medications might significantly improve your symptoms. Occasionally, your health care provider may suggest surgery to regulate certain regions of your brain and improve your symptoms.")
    
    st.header("Symptoms")
    img = Image.open("parkinsons-disease-symptoms-infographic-1200x628.webp")
    
    st.write("Parkinson's disease signs and symptoms can be different for everyone. Early signs may be mild and go unnoticed. Symptoms often begin on one side of the body and usually remain worse on that side, even after symptoms begin to affect the limbs on both sides")
    st.image(img )
    
    st.write("Tremor. A tremor, or rhythmic shaking, usually begins in a limb, often your hand or fingers. You may rub your thumb and forefinger back and forth. This is known as a pill-rolling tremor. Your hand may tremble when it's at rest. The shaking may decrease when you are performing tasks.")
    st.write("Slowed movement (bradykinesia). Over time, Parkinson's disease may slow your movement, making simple tasks difficult and time-consuming. Your steps may become shorter when you walk. It may be difficult to get out of a chair. You may drag or shuffle your feet as you try to walk.")
    st.write("Rigid muscles. Muscle stiffness may occur in any part of your body. The stiff muscles can be painful and limit your range of motion.")
    st.write("Speech changes. You may speak softly, quickly, slur or hesitate before talking. Your speech may be more of a monotone rather than have the usual speech patterns.")
    st.write("Loss of automatic movements. You may have a decreased ability to perform unconscious movements, including blinking, smiling or swinging your arms when you walk.")
    st.write("Writing changes. It may become hard to write, and your writing may appear small")
    st.write("Impaired posture and balance. Your posture may become stooped. Or you may fall or have balance problems as a result of Parkinson's disease.")
   

    st.header("Prevention")
    st.write("Because the cause of Parkinson's is unknown, there are no proven ways to prevent the disease.")
    st.image(img1 , width= 300)
    st.write("Some research has shown that regular aerobic exercise might reduce the risk of Parkinson's disease")
    st.write("Some other research has shown that people who consume caffeine — which is found in coffee, tea and cola — get Parkinson's disease less often than those who don't drink it. Green tea is also related to a reduced risk of developing Parkinson's disease. However, it is still not known whether caffeine protects against getting Parkinson's or is related in some other way. Currently there is not enough evidence to suggest that drinking caffeinated beverages protects against Parkinson's.")



 
# screen_size = pyautogui.size()
if (selected == "Parkinsons Test"):
   
   st.title("Parkinson's Disease Detection Test")
   col1, col2, col3, col4, col5 = st.columns(5)  
   fo = st.text_input('MDVP: Fo(Hz)')
        
   # fhi = st.text_input('MDVP: Fhi(Hz)')
        
   # flo = st.text_input('MDVP: Flo(Hz)')
        
   Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
   # Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
   RAPval = st.text_input('MDVP: RAP')
        
   PPQval = st.text_input('MDVP: PPQ')
        
   DDPval = st.text_input('Jitter: DDP')
        
   Shimmer = st.text_input('MDVP: Shimmer')
        
   Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
   APQ3val = st.text_input('Shimmer: APQ3')
        
   APQ5val = st.text_input('Shimmer: APQ5')
        
   APQval = st.text_input('MDVP: APQ')
        
   DDAval = st.text_input('Shimmer: DDA')
        
   NHRval = st.text_input('NHR')

   HNRval = st.text_input('HNR')
     
   print(type(DDAval))
    

    
   # code for Prediction
   parkinsons_diagnosis = ''
   
   
   st.write("  ")   
   if st.button("Take a Test"):
   
      
      if(fo == '' or Jitter_percent == ''  or RAPval== '' or PPQval == '' or DDPval == '' or Shimmer == '' or  Shimmer_dB == '' or APQ3val == '' or APQ5val == '' or APQval == '' or DDAval == '' or NHRval == '' or HNRval == '' ):
         st.error("Please enter all values correctly!!")

      else:  
         ip =[fo,Jitter_percent, RAPval, PPQval,DDPval,Shimmer,Shimmer_dB,APQ3val,APQ5val,APQval,DDAval,NHRval,HNRval]
         b = np.array(ip, dtype = float) #  convert using numpy
         c = [float(i) for i in ip] #  convert with for loop
         print("after: ", type(DDAval))
         parkinsons_prediction = parkinsons_model.predict([c])                          
         if (parkinsons_prediction == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
            st.warning(parkinsons_diagnosis)
         else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)

      




# python -m streamlit run "C:\Users\HP\Downloads\pd\PARKINSON DISEASES\app.py"
