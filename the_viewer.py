import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('database.csv')
#----------------------Hide Streamlit footer----------------------------
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            layout="wide",
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#--------------------------------------------------------------------
def main():
    #st.title("The Viewer")
    st.markdown("""
        <style>
            body, button, input, select, textarea {
                direction: rtl;
                text-align: right;
                font-family: 'Arial', sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)
    
    df = load_data()
    
    if 'current_row' not in st.session_state:
        st.session_state['current_row'] = 0

    col1, col2 = st.columns(2)
    
    if col1.button("➡️"):
        st.session_state.current_row = max(0, st.session_state.current_row - 1)
    if col2.button("⬅️"):
        st.session_state.current_row = min(len(df) - 1, st.session_state.current_row + 1)
    
    st.header(df.loc[st.session_state.current_row, 'Chapters'])
    st.write(df.loc[st.session_state.current_row, 'text'])

if __name__ == "__main__":
    main()
