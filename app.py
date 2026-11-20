import Streamlit as st
from rag_engine import load_base,ask_rag
st.st_page_config(page_title="SIET_Chatbot",layout="centered")
st.title("Shridevi institute of Engineering and Technology - Chatbot")
st.cption("Ask anything about college information.....")
st.caption("Created by Harshitha raj")

@st.cache_resource
def initiate_rag():
  return load_base("01_College_information.pddf")
  
index,embed_model,chunks=initiate_rag()
