import os
import locale
from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from langchain.llms import GooglePalm
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import google.generativeai as genai

# Set preferred encoding
locale.getpreferredencoding = lambda do_setlocale=True: "UTF-8"

# Configure Google Palm API
genai.configure(api_key='AIzaSyCiEx4VJELwnAjCmGfgZ4ovTKz50pIRJWQ')

# Load Linux document
with open('linux_play.txt') as lin:
    txt_lin = lin.read()
linux_docs = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=20).create_documents([txt_lin])

# Load Space document
with open('space_shortened.csv') as spc:
    txt_spc = spc.read()
space_docs = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=20).create_documents([txt_spc])

# Define HuggingFaceEmbeddings
hfEmbed = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create Chroma vector stores
space_chroma = Chroma.from_documents(documents=space_docs, embeddings=hfEmbed)
lin_chroma = Chroma.from_documents(documents=linux_docs, embeddings=hfEmbed)


# Retrieve questions using the LLM chain
fact_llm = GooglePalm(temperature=0.1)
prompt_template = """Question: {question}\n\nAnswer: Let's think step by step."""
prompt_open = PromptTemplate(
    template=prompt_template, input_variables=["question"])
open_chain = LLMChain(prompt=prompt_open, llm=fact_llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
answer = open_chain.run(question)
print(answer)


# Retrieve answers using the RetrievalQA chain
lin_retriever = RetrievalQA.from_chain_type(
    llm=fact_llm, chain_type="stuff", retriever=lin_chroma.as_retriever())
answer_lin = lin_retriever("What are these documents about?")
print(answer_lin)


space_retriever = RetrievalQA.from_chain_type(
    llm=fact_llm, chain_type="stuff", retriever=space_chroma.as_retriever())
answer_space = space_retriever("How many passengers are there?")
print(answer_space)
