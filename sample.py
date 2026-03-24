from langchain_tavily import TavilySearch
import os, getpass

TAVILY_API_KEY =  os.getenv("TAVILY_API_KEY")
print(TAVILY_API_KEY)