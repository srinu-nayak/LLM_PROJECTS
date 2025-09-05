from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"]




model = ChatOpenAI()


result = model.invoke("what is capital of India?")

print(result.content)

