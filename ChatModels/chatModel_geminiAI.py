from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(
    model= 'gemini-3.5-flash'
)

res = chatModel.invoke("What are attributes of charmendar?")

print(res)
