import numpy as np
import pickle
import streamlit as st
import pandas as pd

Main_data=pd.read_csv('/Users/nags26/Desktop/Next Labs/Data/review_data.csv')
Log_pck= pickle.load(open('/Users/nags26/PycharmProjects/pythonProject/dict.pickle','rb'))

st.title("App Review")

from random import randint

def play():
    random_int = randint(0, 5)

    while True:
        user_guess = int(input("What number do you rate (0-5)?"))

        if user_guess == 3:
            print(f"The review is satisfactory")
            break

        if user_guess < 3:
            print("The review is bad")
            continue
        if user_guess > 3:
            print("The review is very good")
            continue






