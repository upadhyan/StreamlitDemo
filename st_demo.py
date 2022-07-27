import streamlit as st
import nltk
import pandas as pd

def convert_df(df):
   return df.to_csv().encode('utf-8')


nltk.download('punkt')
st.write("""
# Sentence Splitter
The sentence splitter tool allows you to break up large amounts of text into individual sentences. Put a large block of text into the box below and click convert. The tool will then split the text below so that each sentence is on its own line and colored differently from the line above. You can also download the finished result as a word document as well.
""")
title = st.text_input('Text Input', '')
result = nltk.sent_tokenize(title)
hex1 = "#FFC20A"
hex2  = "#0C7BDC"
flag = True
for sentence in result:
    if flag:
        hex = hex1
    else:
        hex = hex2
    flag = not flag
    st.markdown(f"<p style ='color:{hex}'>{sentence}</p>", unsafe_allow_html = True)

