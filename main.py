from helper import document_loader, getAnswerFromLLM
import streamlit as st

st.set_page_config(page_title="FAQ Chatbot", page_icon=":robot:")
st.title("FAQ Chatbot")
st.write("Ask me anything about the FAQ data!")
st.write("Upload your CSV file which contain FAQs First")

try:
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        file_path = uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        data = document_loader(file_path)
        st.write("File uploaded successfully!")
        st.write("You can now ask questions about the data.")

        query = st.text_input("Enter your question:")
        btn = st.button("Get Answer")
        if btn:
            if query:
                with st.spinner("Getting answer..."):
                    answer = getAnswerFromLLM(data, query)
                    st.write(answer)
            else:
                st.warning("Please enter a question.")

except Exception as e:

    if isinstance(e, ValueError):
        st.error(e)
        st.write("Please download the example CSV file below:")
        st.download_button(
            label="Download Example CSV",
            data=open("template.csv", "rb"),
            file_name="example.csv",
            mime="text/csv",
        )
    else:
        st.error(f"Error uploading file: {e}")
