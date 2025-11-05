from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model='gpt-4o', api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = llm.invoke("Say hello")
    print(f"Success! Response: {response.content}")
except Exception as e:
    print(f"Failed: {e}")