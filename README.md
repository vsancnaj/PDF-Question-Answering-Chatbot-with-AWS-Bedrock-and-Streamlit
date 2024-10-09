# PDF Question Answering Chatbot with AWS Bedrock and Streamlit

This project is a multi-language chatbot built with AWS Bedrock and Streamlit. It allows users to upload a PDF document, ask questions about its content in their chosen language, and receive responses based on the content. The project leverages state-of-the-art language models and integrates translation functionality, making it useful for multilingual environments.




https://github.com/user-attachments/assets/f675f6c1-1ca3-4855-96a3-5f9b4fa5db72





### Project Technologies Breakdown

#### 1. **AWS Bedrock**
   AWS Bedrock is the core technology used for the language model in this project. It provides access to powerful, scalable models like Claude from Anthropic, which are used to understand and answer questions about the text extracted from PDF files.

   - **Purpose**: LLM (Language Model) handling for natural language processing.
   - **Used for**: Generating responses based on PDF content.

#### 2. **Boto3**
   Boto3 is the official AWS SDK for Python, used here to interact with AWS Bedrock and manage cloud resources.

   - **Purpose**: Communicate with AWS services (Bedrock).
   - **Used for**: Instantiating Bedrock clients and invoking models.

#### 3. **LangChain**
   LangChain simplifies working with language models by providing utilities for prompt creation and chaining models. It is used to manage the interaction between the PDF content and AWS Bedrock.

   - **Purpose**: To streamline the interactions between the prompt and the LLM.
   - **Used for**: Structuring the prompt that gets sent to the Claude model on AWS Bedrock.

#### 4. **PyMuPDF (fitz)**
   PyMuPDF is used to extract text from uploaded PDF documents. This text is fed into the language model, allowing the chatbot to answer questions about it.

   - **Purpose**: Extract text from PDFs.
   - **Used for**: Parsing and extracting text content from the uploaded PDF document.

#### 5. **Googletrans**
   Googletrans provides real-time translation between languages. It is used in this project to translate questions and answers between English and other supported languages.

   - **Purpose**: Translate input questions and output responses.
   - **Used for**: Handling multilingual input/output for the chatbot.

#### 6. **Streamlit**
   Streamlit is the framework used to build the web-based interface of the project. It allows users to upload PDF documents, select languages, and interact with the chatbot.

   - **Purpose**: Create a web application for user interaction.
   - **Used for**: Uploading PDFs, displaying extracted content, and managing language selection and user input.
