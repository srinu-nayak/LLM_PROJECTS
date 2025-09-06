from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ["OPENAI_API_KEY"]


parser = StrOutputParser()

model = ChatOpenAI()




english_to_spanish = PromptTemplate(
    template="Translate this to Spanish: {text}",
    input_variables=["text"]
    )

english_to_french =  PromptTemplate(template= "Translate this to French: {text}", input_variables=["text"])

english_to_german = PromptTemplate(template="Translate this to German: {text}", input_variables=["text"])

translations = RunnableParallel({
    "spanish" : RunnableSequence(english_to_spanish | model | parser),
    "french" : RunnableSequence(english_to_french | model | parser),
    "german" : RunnableSequence(english_to_german | model | parser) 

})

result = translations.invoke("Artificial intelligence is transforming industries worldwide.")

print(result)


translations.get_graph().print_ascii()