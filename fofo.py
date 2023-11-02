import streamlit as st
import pandas as pd

def main():
    st.title("Admin Page")
    
    new_chapter = st.text_input("New Chapter")
    new_text = st.text_area("New Text")
    
    if st.button("Add Row"):
        new_data = {'Chapters': [new_chapter], 'text': [new_text]}
        df = pd.read_csv('database.csv')
        new_df = pd.DataFrame(new_data)
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv('database.csv', index=False)
        st.success("Row added successfully!")

if __name__ == "__main__":
    main()
