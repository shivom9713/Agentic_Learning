from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages  ## Optimized reducer with BaseMessage Class
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from my_llm import *
from langchain_core.runnables import RunnableConfig
from langchain.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition 
import sqlite3
from tools import calculate, search_tool, get_stock_price


class ChatState(TypedDict): # Inherits from the TypedDict Class
    messages: Annotated[list[BaseMessage], add_messages]


def ChatNode(state: ChatState):
    """LLM node that may answer or request a tool call."""
    # take user query
    messages = state['messages']

    
    # send to LLM
    response = model_with_tools.invoke(messages)
    print(response)
    # Append to state
    return {'messages':[response]}

tools = [calculate, search_tool, get_stock_price]
tool_node = ToolNode(tools)
model_with_tools = model.bind_tools(tools)

connection_object = sqlite3.connect(database='./DB/chatbot3.db', check_same_thread=False) ## Check same thread is False because SQLite is single threaded by default. 

# Define graph
graph = StateGraph(ChatState)

# Add nodes
graph.add_node("ChatNode",ChatNode)
graph.add_node("tools",tool_node)

## Connect
graph.set_entry_point("ChatNode")
graph.add_conditional_edges("ChatNode", tools_condition)
graph.add_edge("tools","ChatNode")

## To save the checkpoints
checkpointer = SqliteSaver(connection_object) 
workflow = graph.compile(checkpointer=checkpointer)



# print(list(set(x.config['configurable']['thread_id'] for x in checkpointer.list(None))))




