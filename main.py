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
    and a tiny bit of swift. I'm currently attending UVU, studying computer science.
    I also attended Devmountain in 2022 and graduated in their web development program. 
    I gained experience in HTML/CSS, react, javascript, SQL and node.js. 
    I also have sales experience, working in tech sales for a company here in Utah.
    In my free time I love to play tennis and golf, and spend time with my wife and daughter.
    """
    st.write(content)
