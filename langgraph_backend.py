from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages  ## Optimized reducer with BaseMessage Class
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from my_llm import *
from langchain_core.runnables import RunnableConfig
import sqlite3


class ChatState(TypedDict): # Inherits from the TypedDict Class
    messages: Annotated[list[BaseMessage], add_messages]


def ChatNode(state: ChatState):

    # take user query
    messages = state['messages']

    # send to LLM
    response = AIMessage(model.invoke(messages).content)
    
    # Append to state
    return {'messages':[response]}

connection_object = sqlite3.connect(database='./DB/chatbot3.db', check_same_thread=False) ## Check same thread is False because SQLite is single threaded by default. 

# Define graph
graph = StateGraph(ChatState)

# Add nodes
graph.add_node("ChatNode",ChatNode)

## Connect
graph.set_entry_point("ChatNode")
graph.add_edge("ChatNode",END)

## To save the checkpoints
checkpointer = SqliteSaver(connection_object) 
workflow = graph.compile(checkpointer=checkpointer)


# config: RunnableConfig = {"configurable": {"thread_id": 'thread-1'}}
# response = workflow.invoke({'messages':[HumanMessage(content='What are India and pakistan, answer using my name ... ')]},
#                 config = config)
# print(list(set(x.config['configurable']['thread_id'] for x in checkpointer.list(None))))




