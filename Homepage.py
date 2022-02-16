import streamlit as st

def Homepage():
    Home_sidebar()
    Home_body()

def Home_sidebar():
    st.sidebar.write("""
    #### Some of my works: \n
    [Github](https://github.com/hungha11) \n
    [LinkedIn](https://www.linkedin.com/in/quốc-hùng-hà-6b192b222/)\n
    [Facebook](https://www.facebook.com/ha.quoc.hung11)
    """)


def Home_body():
    st.write('##### Some of the information about myself:')
    st.write("""
    I am a student at RMIT University in Vietnam. \n
    With the enthusiasm of learning new things, I am always looking for new challenges. \n
    Although my major is Economics and Finance, I am also interested in Machine Learning and Data Science, 
    especially its application in Algorithmic Trading. \n 
    I am a self-taught programmer and I am always trying to improve my skills. Additionally, you can contact me at: \n
        qhung9621@gmail.com
        
    #
    #
    """)

    st.write("""
    ##### About this project: \n
    The purpose of this project is to be the place that I can store my projects and share them with others. \n
    Currently, there are two big parts, which is Streamlit and Algorithmic Trading code.
    I hope in the near future, I can fill the Machine Learning and Statistics page.   \n
    ***
    The project is written in python and built on the Streamlit framework. \n
    Some of the interesting libraries that I used are: \n
    - For data source:
        - [vnquant](https://github.com/phamdinhkhanh/vnquant) \n
        - [investpy](https://investpy.readthedocs.io)
    - For plotting:
        - [plotly](https://plot.ly/python/) \n
        - [mplfinance](https://github.com/matplotlib/mplfinance) \n
    """)