import streamlit as st
import math as az

from zmq import HELLO_MSG
st.header('This is an example of how a header looks')
st.subheader('This is an example of subheader')
st.button('Clickkable')

st.title('Simplicty, Redefined.')
st.caption("This is an example of how caption look")
st.code("""

def Function(num):
    a=1
    b=2
    return num-a+b 
    #It is going to give the value as the output of this function.

print(Function(90)) #Output = 90-1+2 = '91'


""")
