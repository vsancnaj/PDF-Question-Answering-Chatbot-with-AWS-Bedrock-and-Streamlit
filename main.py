import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
from langchain_aws import ChatBedrock
from langchain.prompts import PromptTemplate
import boto3
import os
from googletrans import Translator

# Set your AWS profile for Boto3 to use
os.environ["AWS_PROFILE"] = "valentina"

# Create Bedrock client to interact with Bedrock models
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"  # Ensure Bedrock is available in this region
)

# Model ID for the Claude model from Anthropic
modelID = "anthropic.claude-3-sonnet-20240229-v1:0"

# Create the Bedrock LLM instance using the client and model ID
llm = ChatBedrock(
    client=bedrock_client,
    model_id=modelID
)

# Language Translator 
translator = Translator()

def extract_text_from_pdf(pdf_file):
    """Extract text from the uploaded PDF file."""
    pdf_text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            pdf_text += page.get_text()
    return pdf_text

def my_pdf_chatbot(language, text, question):
    """Chatbot that answers questions about the PDF content in the desired language."""
    # Translate the question into English
    if language != "english":
        translated_question = translator.translate(question, src=language, dest="en").text
    else:
        translated_question = question

    # Create a prompt for the model with the PDF content
    prompt = PromptTemplate(
        input_variables=["pdf_content", "question"],
        template="You are an assistant that understands PDF documents. Here's the content:\n\n{pdf_content}\n\nPlease answer this question based on the document: {question}."
    )

    bedrock_chain = prompt | llm

    # Get the response from the LLM
    response = bedrock_chain.invoke({'pdf_content': text, 'question': translated_question})

    # Translate the response back to the desired language if necessary
    if language != "english":
        translated_response = translator.translate(response.content, src="en", dest=language).text
    else:
        translated_response = response.content

    return translated_response

# STREAMLIT - Interface
st.title("PDF Question Answering Chatbot")

# Sidebar for language selection
language = st.sidebar.selectbox("Choose a language", ["english", "spanish", "french", "german", "chinese"])

# PDF Upload
uploaded_pdf = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_pdf:
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(uploaded_pdf)
    
    # Display the extracted PDF content (optional, for debugging)
    st.write("Extracted PDF Content (Preview):")
    st.text_area("", pdf_text[:1000], height=200)  # Only show the first 1000 characters for brevity

    # Ask a question about the PDF content
    question = st.text_area("Ask a question about the PDF")

    if question:
        response = my_pdf_chatbot(language, pdf_text, question)
        st.write("Answer:")
        st.write(response)
