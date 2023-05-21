
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import  initialize_agent, tools, AgentType

def lookup(name: str) -> str:
    return "Linkedin Profile URL"