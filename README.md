# ChatBot with LLM #
A simple chat application that uses LLM's with embedding models and vector stores and built with StreamLit.

## Screenshot ##
![image](https://github.com/user-attachments/assets/999da83f-5599-4b43-b64a-67658d699615)

## Installation ##

1. Clone the repository:
     ```bash
     https://github.com/joaovbez/embeddings_llm.git

2. Navigate to the project folder:
   ```bash
     cd folder_path

3. Create an virtual environment:
   ```bash
     python3 -m venv .venv
Or simply go to View > Command palette > Create virtual environment, on VS Code

4. Install the required dependencies:
   ```bash
   pip install -r .\requirements.txt

5. The following models were used in this project:
   - OpenAI LLM model, with an API KEY 
   - OpenAI Embeddings model, with an API KEY
   - FAISS Vector Store, free.

   If you also use templates that require an API KEY, don't forget to pass it through environment variables.
   ```bash
   import os
   from dotenv import load_dotenv

   # With the API_KEY storaged on .env archive created, make:
   load_dotenv()  

6. Run the application
   ```bash
   streamlit run app.py
