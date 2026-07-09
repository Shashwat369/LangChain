from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModels = GoogleGenerativeAI(
    model= 'gemini-3.5-flash',
    temperature = 0
)


result = chatModels.invoke("What is the capital of india?") #statement inside invoke is known as prompt

print(result.content)

