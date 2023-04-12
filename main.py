import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Matt Moon")
    content = """
    Hi, I'm Matt. I am a 23 year old Account Executive/Programmer. 
    I have experience in web development, python, 
    and a tiny bit of swift.
    """
    st.write(content)
