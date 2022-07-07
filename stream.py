import streamlit as st
st.header('WELCOME TO MY APP')
x=st.number_input('Put your first number here')
y=st.number_input('put your secound number here')
z=x+y
on_sale={'Amala':500,'Banga':350,'Rice':100,'spag':200,'pie':400}
food=[on_sale.keys()]
st.selectbox('please select your food',food)
price=on_sale.values()
st.write(f'your purchase of {food} cost #{price}')
