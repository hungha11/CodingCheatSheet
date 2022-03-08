import  streamlit as st
from Homepage import *
from Streamlit_page import *
from AlgoTrade import *
from MachineLearning import *
from Statistics import *
from Autotrader import *
import PIL.Image

# Initial page config
st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="collapsed",
)


if __name__ == "__main__":
    st.markdown("""
    <style>
    body {
      background: #ff0099; 
      background: -webkit-linear-gradient(to right, #ff0099, #493240); 
      background: linear-gradient(to right, #ff0099, #493240); 
    }
    </style>
        """, unsafe_allow_html=True)

    st.markdown(f'''
                <style>
                    section[data-testid="stSidebar"] .css-ng1t4o {{width: 16rem;}}
                    section[data-testid="stSidebar"] .css-1d391kg {{width: 16rem;}}
                </style>
            ''', unsafe_allow_html=True)


    page = st.sidebar.selectbox('Choose a page',
                                ['Home', 'Streamlit' ,'Algorithmic Trading','Statistics','Machine learning','Autotrader'])
    #page title
    st.markdown("<h1 style='text-align: center; color: orange;'>Coding cheat sheet</h1>", unsafe_allow_html=True)

    #background colot

    if page == 'Home':
        st.write("""
        #
        """)
        col1,col2 = st.columns(2)
        with col1:
            Homepage()
        with col2:
            image = PIL.Image.open('image.JPG')
            st.image(image,width=500)
    if page == 'Streamlit':
        Streamlit()
    if page == 'Algorithmic Trading':
        st.title('Algorithmic Trading')
        AlgoTrade()
    if page == 'Statistics':
        st.title('Statistics')
        st.markdown('This is a statistics page')
        Statistics()
    if page == 'Machine learning':
        st.title('Machine learning')
        MachineLearning()
    if page == 'Autotrader':
        st.title('Autotrader')
        Autotrader()

