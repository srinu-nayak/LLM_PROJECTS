from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["HUGGINGFACEHUN_ACCESS_KEY"]


model = ChatHuggingFace(llm = HuggingFaceEndpoint(
    repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
))



result = model.invoke("what is the capital of france?")
print(result)


