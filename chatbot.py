import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


prompt = """
You are a Financial Analytics Agent
"""

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', prompt),
        ('placeholder', '{messages}')
    ]
)

llm  = ChatOpenAI(
    model = 'gpt-4o',
    temperature=0,
    max_tokens=None

)

llm_with_prompt = chat_template | llm

def call_agent(message_state: MessagesState):
    response = llm_with_prompt.invoke(message_state)
    return {
        'messages': [response]
    }



graph = StateGraph(MessagesState)
graph.add_node('agent', call_agent)
graph.add_edge('agent', '__end__')
graph.set_entry_point('agent')

app = graph.compile()


