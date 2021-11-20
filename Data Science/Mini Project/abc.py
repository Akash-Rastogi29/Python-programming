from logging import PlaceHolder
from sqlalchemy.orm.session import Session
import streamlit as st
from database import Password
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, engine

engine = create_engine('sqlite:///mydatabase.sqlite3', connect_args
 = {'check_same_thread': False})
Session = sessionmaker(engine)
session = Session()

sidebar = st.sidebar

sidebar.header("Welcome! choose your option here")
sidebar.markdown("---")

options = ['SignUp', 'Login']

selOp = sidebar.selectbox('Select Option', options)

def signUp():
    st.title("Set Password")
    Username = st.text_input("Username:", help= "Enter Username here")
    Password = st.text_input("Password:", help= "Enter Password here")
    btn = st.button("Submit")
    if btn:
        try:
            pass = Passwords(username = Username , password = Password)

            session.add(pass)
            session.commit()

            st.success('Data Saved!!')
        except Exception as e:
            print(e)
            st.error('Error in saving data')


def Login():
    st.title("Login")
    Username1 = st.text_input("Username")
    Password1 = st.text_input("Password")
    btn1 = st.button("Submit")

if selOp == options[0]:
    signUp()
elif selOp == options[1]:
    Login()