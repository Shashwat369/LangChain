from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model= 'gemini-embedding-001', output_dimensionality=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggresive batting and leadership.",
    "MS Dhoni is a former Indian captian famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket holds many batting records.",
    "Rohit Sharma is known for hsi elegant batting and recors-breaking double centuries."
    ]

query = "tell me about virat kohli"

vectorized_documents = embedding.embed_documents(documents)
vectorized_query = embedding.embed_query(query)

scores = cosine_similarity([vectorized_query], vectorized_documents)[0]

index , score = sorted(list(enumerate(scores)), key= lambda x:x[1])[-1]

print(query)
print(documents[index])
print(f"Similarity score is : {score}")