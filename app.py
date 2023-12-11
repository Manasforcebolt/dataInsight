import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import time
from streamlit_pandas_profiling import st_profile_report

def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html= True)

st.set_page_config(layout="wide")
load_css("style.css")

st.title("Data-Insight: Know the hidden insights of your data")


file = st.sidebar.file_uploader("Upload your data file in csv", type='csv')

if file:
    df = pd.read_csv(file)
    with st.spinner("Getting Insights ..."):
        time.sleep(5)
    st.success("Completed!!")
    st_profile_report(df.profile_report())

else:
    st.warning("Please upload the data in the csv format.")
