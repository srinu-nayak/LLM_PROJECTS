from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"]




model = OpenAI()


result = model.invoke("what is capital of India?")

print(result)

