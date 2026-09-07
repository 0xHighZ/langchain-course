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


llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.0,
    )

tools = [TavilySearch()]
# tools = [search]
agent = create_agent(model=llm, tools=tools)
my_query = "search for 3 job posting for an ai engineer using langchain in argentina on linkedin and list their details"
def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content=my_query)})
    print(result)


if __name__ == "__main__":
    main()
