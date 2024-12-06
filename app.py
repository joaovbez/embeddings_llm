import getpass
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms.openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
file_path = "edital_2025.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 250, 
                                                 chunk_overlap = 100, 
                                                 add_start_index = True)
  
all_splits = text_splitter.split_documents(docs)
  
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = FAISS.from_documents(all_splits, embeddings)

def process_prompt(prompt):
  prompt_template = ChatPromptTemplate([
    ("system", """Você é um especialista no documental Edital do vestibular do Instituto tecnológico de Aeronáutica para o ano de 2025. 
                  Sua função é tirar qualquer dúvida do usuário sobre o vestibular a partir do prompt fornecido a você, que conterá informações
                  chaves para que você responda o usuário"""),
    ("user", """A dúvida do usuário é {prompt}. Você deve respondê-lo da melhor forma possível com base na seguintes informações,
                que foram retirada diretamente do arquivo do edital e possuem semelhança com o que o usuário solicitou:
                {similarity_search}""")
  ])

  similarity_search = [doc.page_content for doc in vector_store.similarity_search(prompt, k = 5)] 
  
  return prompt_template.invoke({"prompt":prompt, "similarity_search": similarity_search})


def pagina_chat():
  st.title("Vestibular ITA 2025")
  st.write("Um assistente tecnológico com IA para tirar suas dúvidas sobre nosso vestibular!")
  prompt = st.text_input("Pergunte algo para nossa inteligência artifical possa responder...")

  if st.button("Enviar"):
    if prompt:  
      with st.spinner("Gerando resposta..."):
        query = process_prompt(prompt)
        st.write(llm.invoke(query).content)
         
  
if __name__ == '__main__':

  llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

  pagina_chat()

