from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity
 
load_dotenv()

os.environ["OPENAI_API_KEY"]



embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)


documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

query = "Which city is the capital of France?"

embedded_documents = embeddings.embed_documents(documents)

embedded_query = embeddings.embed_query(query)


scores = cosine_similarity([embedded_query], embedded_documents)[0]

index, score = sorted(list(enumerate(scores)), key= lambda x:x[1])[-1]

print(documents[index])
print(score)
