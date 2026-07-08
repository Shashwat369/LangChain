from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-3.5-flash"
)

response = llm.invoke("Who is Virat Kohli?")

print(response)