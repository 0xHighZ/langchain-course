from typing import List
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
# from tavily import TavilyClient  # use for custom tool definition
from langchain_tavily import TavilySearch # use when tavily implamentation is preferred


load_dotenv()

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)

class Source(BaseModel):
    """Schema for a source used by the agent
    """
    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for the agent response with answer and sources"""
    answer: str = Field(description="The agent's answer to the query")
    sources: list[Source] = Field(default_factory=list, description="List of sources used to generate the answer")


llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.0,
    )

tools = [TavilySearch()]

# Instrucción clave para obligar al LLM a investigar primero
system_prompt = (
    "You are an expert researcher. You must ALWAYS use TavilySearch to gather external "
    "information before producing your final answer. If searching for LinkedIn jobs, "
    "search public job postings via search queries."
)


# tools = [search]
agent = create_agent(model=llm, tools=tools, system_prompt=system_prompt, response_format=AgentResponse)
my_query = "search for 3 job posting for an ai engineer using langchain in argentina on linkedin and list their details"
def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content=my_query)})
    # Imprimir directamente la salida estructurada limpia
    if "structured_response" in result:
        res = result["structured_response"]
        print("\n--- RESPUESTA ---")
        print(res.answer)
        print("\n--- FUENTES ---")
        for src in res.sources:
            print(f"- {src.url}")
    else:
        print(result)


if __name__ == "__main__":
    main()
