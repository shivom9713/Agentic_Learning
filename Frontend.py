
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, AIMessageChunk
import streamlit as st
from langgraph_backend_tools import *
from utils import *
from prompts import *
import yaml
import os
import uuid


######################## SESSION INIT #########################

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = create_thread_id()

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# FIX: chat_threads must be a list of thread_ids, not sets
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = list(set(x.config['configurable']['thread_id'] for x in checkpointer.list(None)))

if 'current_chat_thread_name' not in st.session_state: ### Must be a UUID object
    st.session_state['current_chat_thread_name'] = str(st.session_state['thread_id'])

if 'is_chat_named' not in st.session_state: ### Must be a UUID object
    st.session_state['is_chat_named'] = False



# --- Ensure current thread exists in YAML ---
thread_id_str = str(st.session_state["thread_id"])
append_chat_thread(thread_id_str, thread_id_str)

# print(load_or_create_yaml())

######################## SIDE BAR #############################

st.sidebar.header("My Chats")

# -------------------- NEW CHAT BUTTON ------------------------
if st.sidebar.button("New Chat"):
    st.session_state['thread_id'] = create_thread_id()
    new_thread = st.session_state['thread_id']

    # Clear message history
    st.session_state['message_history'] = []

    # Add to chat thread list
    st.session_state['chat_threads'].append(new_thread)

    append_chat_thread(str(new_thread),chat_name=str(new_thread))

    st.session_state['current_chat_thread_name'] = str(st.session_state['thread_id'])
    st.session_state['is_chat_named'] = False
    st.rerun()


# -------------------- LOAD OLD CHATS --------------------------
st.sidebar.header("Load Conversations")
chat_list = load_or_create_yaml()
chat_list = chat_list["chats"] # returns a dictionary {"thread_id":{details}}
# print(chat_list, "chat list")
# Reverse list: show newest first
for thread in reversed(st.session_state['chat_threads']):
    thread_key = str(thread)
    chat_name = chat_list[thread_key]["chatname"]
    # print(chat_name, "chat name")

    if st.sidebar.button(str(chat_name)):
        st.session_state['thread_id'] = thread
        st.session_state['current_chat_thread_name'] = chat_name
        st.session_state['message_history'] = []
        st.session_state['is_chat_named'] = chat_list[thread_key]["is_updated"]

        # Retrieve conversation from LangGraph
        config = {"configurable": {"thread_id": thread}}

        try:
            state = workflow.get_state(config=config)
            raw_history = state.values['messages']

            parsed = []
            for msg in raw_history:
                if isinstance(msg, HumanMessage):
                    parsed.append({"role": "user", "content": msg.content})
                elif isinstance(msg, AIMessage):
                    parsed.append({"role": "assistant", "content": msg.content})

            st.session_state['message_history'] = parsed

        except Exception as e:
            print("ERROR LOADING THREAD:", e)

        st.rerun()

###############################################################




######################## SHOW CHAT HISTORY ####################

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])



######################## USER INPUT ###########################

user_input = st.chat_input("Type your question here")

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})

    with st.chat_message("user"):
        st.write(user_input)

    config = {"configurable": {"thread_id": st.session_state['thread_id']},
    "metadata":{"thread_id": st.session_state['thread_id']}, ### This is important for LangGraph to map thread for tracability and debugging  
    "run_name":"chat_turn"  ### For better traceability in LangGraph, we name each run as "chat_turn"
    }

    # Stream AI response
    def ai_token_gen(user_input, config):
        final_text = None
        for chunk, metadata in workflow.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config=config,
            stream_mode="messages"
        ):
        
            if isinstance(chunk, AIMessageChunk) and chunk.content:
                yield chunk.content

             
            elif isinstance(chunk, AIMessage):
                final_text = chunk.content
        return final_text

    
    with st.spinner("Generating Response ...", show_time=True):
        with st.chat_message("assistant"):
            placeholder = st.empty()
            final_full_text = placeholder.write_stream(ai_token_gen(user_input, config))

    

    st.session_state['message_history'].append({'role': 'assistant', 'content': final_full_text})

    # --- Auto-generate chat name ---
    try:
        # print("chat named???",st.session_state['is_chat_named'])
        if len(st.session_state['message_history']) > 1 and st.session_state['is_chat_named'] == False :
            # print("Renaming Chats")
            chain = chat_naming_prompt | model.with_structured_output(ChatName)
            chat_name = chain.invoke({"message_history": st.session_state['message_history']})

            st.session_state['current_chat_thread_name'] = chat_name.chat_name
            st.session_state['is_chat_named'] = True

            # Save back to YAML
            update_chat_thread(str(st.session_state['thread_id']), chat_name=st.session_state['current_chat_thread_name'])

    except Exception as e:
        print("Chat name generation error:", e)

    st.rerun()

###############################################################
