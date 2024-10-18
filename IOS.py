import streamlit as st

#with open('exemplo.html', 'r') as f:
with open('map-pe-24.html', 'r') as f:
    html_string = f.read()

st.header('Votação Por Bairro - 2024')

#st.components.v1.html(html_string, height=500)
st.components.v1.html(html_string, height=700)