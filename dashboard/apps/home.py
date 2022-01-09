import streamlit as st
from numpy import random

def app():
    st.title('Homepage')

    st.write('Bienvenidos a la web de estudios de pingüinos')

    g = ["https://media.giphy.com/media/jKIP9X4OvtyBW/giphy.gif", "https://media.giphy.com/media/DqY8dWBiMus24/giphy.gif", "https://media.giphy.com/media/gbjAtqpO716Hm/giphy.gif", "https://media.giphy.com/media/rSzvcaltZQTm/giphy.gif", "https://media.giphy.com/media/C9AuY1VOvurxm/giphy.gif"]
    
    

    gif = g[random.randint(5)]
    _left, mid, _right = st.columns(3)
    with _left:
        st.image(gif, width=800)