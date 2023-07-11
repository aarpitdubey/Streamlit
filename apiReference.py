import streamlit as st
import pandas as pd

st.write('Hello, **world**!')

# magic command

"Hello, **world**!"

# for caption

st.caption("This is string")

# for code

code = '''
def hello():
    print("Hello, world! This is Arpit")
'''
st.code(code)

# for text

st.text(" Welcome Arpit Dubey ji")

# for latex 

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
