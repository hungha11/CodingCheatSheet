import streamlit as st


def MachineLearning():
    ML_sidebar()
    ML_body()


def ML_sidebar():
    st.sidebar.write("""***""")

    st.sidebar.write("""
    ### Some of the inportant resources:
    - #### Vietnamese sources:
        - [Pham Dinh Khanh](https://phamdinhkhanh.github.io/deepai-book/intro.html)
        - [Machine learning co ban](https://machinelearningcoban.com)

    - #### English sources:
        - [Machine learning mastery](https://machinelearningmastery.com)
        - [100 days of  ML code](https://github.com/Avik-Jain/100-Days-Of-ML-Code)
    """)
    st.sidebar.write("""***""")
    st.sidebar.write("""
    ### Hosting platform
    - [Google Collab](https://colab.research.google.com/notebooks/welcome.ipynb)
    """)


def ML_body():
    st.write('Machine Learning')
    st.write('Still working on it')