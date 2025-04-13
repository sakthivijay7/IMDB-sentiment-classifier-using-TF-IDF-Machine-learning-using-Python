import streamlit as st
import joblib

with open("nlptrained.pkl","rb") as f:
    trained_model=joblib.load(f)
    model=trained_model["Logistic Regression"]  

with open("vectorizer.pkl","rb") as f:
    vectorizer=joblib.load(f)  
   
   
st.title("IMDB Movie Review sentiment classifier")
review=st.text_area("Enter your review ")
if st.button("Predict") :
    vec=vectorizer.transform([review])
    predict=model.predict(vec)
    if predict ==1:
        st.success("Positive")
    else:
        st.error ("Negative")  


