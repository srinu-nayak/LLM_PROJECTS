from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ["OPENAI_API_KEY"]


parser = StrOutputParser()

model = ChatOpenAI()

#prompt 1
prompt1 = PromptTemplate(
    template="Generate a quote on a give {topic}",
    input_variables=["topic"],
    validate_template=True
)

#prompt 2
prompt2 = PromptTemplate(
    template="Give me the 5 quotes based on given {text}",
    input_variables=["text"],
    validate_template=True
)




chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "study"})
print(result)