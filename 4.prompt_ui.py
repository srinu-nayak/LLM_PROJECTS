from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st
import os



load_dotenv()
os.environ["OPENAI_API_KEY"]

model = ChatOpenAI()

st.header('Reasearch Tool')



paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

prompt_template_json = load_prompt("template.json")



if st.button('Summarize'):
    chain = prompt_template_json | model
    
    result = chain.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input, 
            "length_input": length_input
        }
    )

    st.write(result.content)
    