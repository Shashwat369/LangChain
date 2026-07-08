from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(
    model= 'gemini-3.5-flash',
    temperature= 1.5, # This basically shows how creative your response will be if it 0 then it is normal and if it is more than 1.5 then the response will be highly creative
    max_completion_tokens = 10 # And this is used to limit the usage of the token like putting a limit to token usage.
)

res = chatModel.invoke("What are attributes of charmendar?")

print(res.content)
