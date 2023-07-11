import streamlit as st
import pandas as pd

# title
st.title("Hello, Welcome Arpit Dubey ji")

# header
st.header("This is a header")

# sub header
st.header("This is a sub header")

Data = {
    "Company": ["google", "Apple", "Meta"],
    "Salary": ["$800000", "$600000","$700000"],
    "Language": ["python", "Java", "C++"]
}

st.write(Data)

st.write(pd.DataFrame(Data))

st.markdown("""This is a Mark down file.
# h1 tag
## h2 tag
### h3 tag """)