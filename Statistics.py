import streamlit as st

def Statistics():
    Statistics_sidebar()
    Statistics_main()

def Statistics_sidebar():
    st.sidebar.title("Statistics")
    st.sidebar.info("""
    This page contains some statistics about the data.
    """)

def Statistics_main():
    st.write('Working on it...')
    st.latex(r'''
    \begin{align}
        v_{avg} &= \frac{\left( v_{i} + v_{f} \right)}{2} \\
        \Delta x &= v_{avg} t \\
        a &= \frac{\left( v_{f} - v_{i} \right)}{t} \\
    \end{align}
    ''')
