import streamlit as st
def Streamlit():
    Streamlit_sidebar()
    Streamlit_body()

    return None

def Streamlit_sidebar():
    st.sidebar.write('This is Streamlit sidebar')

def Streamlit_body():
    st.write('This is Streamlit body')
    col1, col2, col3 = st.columns(3)
    col1.subheader('Frequently used funtions')
    col1.code('''
    #Add the html 
    HtmlFile = open("html/indexChart.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=600, width=1000, )
    ''')