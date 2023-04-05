

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit.components.v1 import html

# import pyautogui

# loading the saved models

parkinsons_model = pickle.load(open("parkinsons_detection_model.sav", 'rb'))



# sidebar for navigation
with st.sidebar:
    # st.title("Parkinson's Disease Detection using Machine Learning")
    selected = option_menu('Parkinsons Disease Detection',
                          
                          ['About', 'Parkinsons Test'],
                          icons=['person','pen',],
                          default_index=0)
    

# Parkinson's Prediction 
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
    i = 0
    if(i <= 768):
   #  if(screen_size.width <= 768):
        fo = st.text_input('MDVP: Fo(Hz)')
        
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
        flo = st.text_input('MDVP: Flo(Hz)')
        
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        Jitter_percent = int(Jitter_percent)
        Jitter_percent = Jitter_percent/100
        Jitter_percent = str(Jitter_percent)
        
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
        RAP = st.text_input('MDVP: RAP')
       
        
        PPQ = st.text_input('MDVP: PPQ')
      
        
        DDP = st.text_input('Jitter: DDP')
     
        
        Shimmer = st.text_input('MDVP: Shimmer')
        
        
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
        APQ3 = st.text_input('Shimmer: APQ3')
       
        
        APQ5 = st.text_input('Shimmer: APQ5')
        
        
        APQ = st.text_input('MDVP: APQ11')
        
        
        DDA = st.text_input('Shimmer: DDA')
        
        
        NHR = st.text_input('NHR')

        HNR = st.text_input('HNR')
     

    
    else:
     with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
        
     with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
     with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
        
     with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
     with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
     with col1:
        RAP = st.text_input('MDVP: RAP')
        
     with col2:
        PPQ = st.text_input('MDVP: PPQ')
        
     with col3:
        DDP = st.text_input('Jitter: DDP')
        
     with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
        
     with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
     with col1:
        APQ3 = st.text_input('Shimmer: APQ3')
        
     with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
        
     with col3:
        APQ = st.text_input('MDVP: APQ')
        
     with col4:
        DDA = st.text_input('Shimmer: DDA')
        
     with col5:
        NHR = st.text_input('NHR')
        
     with col1:
        HNR = st.text_input('HNR')
        
    


    

    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction 
    st.write("  ")   
    if st.button("Take a Test"):
   
        # if(fo == '' or fhi == '' or flo == '' or Jitter_percent == '' or Jitter_Abs == '' or RAP == '' or PPQ == '' or DDP == '' or Shimmer == '' or  Shimmer_dB == '' or APQ3 == '' or APQ5 == '' or APQ == '' or DDA == '' or NHR == '' or HNR == '' or RPDE == '' or DFA == '' or spread1 == '' or spread2 == '' or D2 == ''  or PPE == '' ):
        #  st.error("Please enter all values correctly!!")
        if(fo == '' or fhi == '' or flo == '' or Jitter_percent == '' or Jitter_Abs == '' or RAP == '' or PPQ == '' or DDP == '' or Shimmer == '' or  Shimmer_dB == '' or APQ3 == '' or APQ5 == '' or APQ == '' or DDA == '' or NHR == '' or HNR == '' ):
         st.error("Please enter all values correctly!!")


        else: 
          
        #   parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent/100, Jitter_Abs, RAP/100, PPQ/100,DDP/100,Shimmer/100,Shimmer_dB,APQ3/100,APQ5/100,APQ/100,DDA/100,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
          parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR]])                          
           
          if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
            st.warning(parkinsons_diagnosis)
          else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)




# python -m streamlit run "C:\Users\HP\Downloads\pd\PARKINSON DISEASES\app.py"
