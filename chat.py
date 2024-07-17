import streamlit as st
from pdf_processing import PDF_Processing 
st.title("PDF BOT")

file = st.file_uploader("upload your pdf here")
obj = None
if file:
    with open("./input_pdf/new_uploaded_pdf.pdf","wb") as f:
        f.write(file.getbuffer())
    #st.write("Processing")
    obj = PDF_Processing(path="./input_pdf/")
    st.subheader("We are all set")


if file:
        
        if "messsages" not in st.session_state:
            st.session_state.messages = []


        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["message"])

        prompt = st.chat_input("Ask questions on pdf here")
        response = "This is a pdf qThis is a pdf question answering bot"
        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role":"user","message":prompt})
            response = obj.query_the_pdf(prompt) 
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role":"assistant","message":response})
    