from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
llm= ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

#response=llm.invoke("Hi how are you")
#print(response.comtent)
st.title("Chatbot")
response= st.text_input("Enter your text here:")
if st.button("Submit"):
    result=llm.invoke(response)
    st.write(result.content)