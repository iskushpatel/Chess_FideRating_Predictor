
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_note(blitz, rapid, bullet):
    prediction=classifier.predict([[blitz, rapid, bullet]])
    print(int(prediction))
    return int (prediction)

def main():
    if st.button("About"):
        st.text("This is a simple Chess-Rating Predictor App")
        st.text("Built with Streamlit")
    st.title(" Chess-Rating Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Chess.com Rating to FIDE Rating </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    blitz =int(st.number_input("Chess.com Blitz "))
    rapid = int(st.number_input("Chess.com Rapid "))
    bullet = int(st.number_input("Chess.com Bullet"))
    #entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note(blitz, rapid, bullet)
    st.success('Estimated Fide Rating: {}'.format(result))
    

if __name__=='__main__':
    main()
    
    
    