import streamlit as st
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

importr("palettetown")  # needs "install.packages('palettetown')" in R console beforehand

st.write(robjects.r("pi")[0])
st.write(robjects.r("1+1")[0])
st.write(robjects.r("pokedex"))
