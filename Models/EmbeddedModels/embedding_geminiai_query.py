from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import  load_dotenv

load_dotenv()

embeding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-001', output_dimensionality= 16)

result= embeding.embed_query("Delhi is the capital of india.")

print(str(result))