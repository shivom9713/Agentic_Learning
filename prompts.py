from langchain_core.prompts import ChatPromptTemplate


chat_naming_prompt = ChatPromptTemplate.from_messages([
    ("system", "You create short chat titles (3-8 words), Title Case, no PII/emojis/quotes."),
    ("user", "Chat History:\n{message_history}\n\nReturn 'chat_name' only and nothing else."
    "Chat_name: ")
])
