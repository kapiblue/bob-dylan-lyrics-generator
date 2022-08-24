import os
import streamlit as st
import lyricsgenius as lg

st.title('Bob Dylan Lyrics Generator')

os.environ["GENIUS_ACCESS_TOKEN"] =  st.secrets["GENIUS_ACCESS_TOKEN"]

import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

genius = lg.Genius()
