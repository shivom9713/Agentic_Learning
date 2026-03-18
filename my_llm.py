import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# Load environment variables from the .env file in the current directory
load_dotenv()




model = AzureChatOpenAI(
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    timeout=None,
    max_retries=2,
    disable_streaming = False
)