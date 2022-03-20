from pyexpat import model
import numpy as np
import streamlit as st
import pickle
import pandas as pd

Main_data=pd.read_csv(r'/Users/nags26/Desktop/Next Labs/Data/review_data.csv')

st.title("App Review")

result = model.predict('Text')
print(result)

result = 'Text'
if result == "happy":
    print("The review is not fake")
else:
    print("The review is fake")

i = "Rating"
if  i>3:
    print("The rating is not fake")
else:
    print("The rating is fake")

Q = np.array[(Text, Star)]
Q = Q.reshape(1,2)
st.title
