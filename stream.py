import streamlit as st
st.header('WELCOME TO MY APP')
x=st.number_input('Put your first number here')
y=st.number_input('put your secound number here')
z=x+y
if st.button('calculate'):
    st.write(z)
