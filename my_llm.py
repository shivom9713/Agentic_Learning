import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
# import os
from langchain_google_genai import ChatGoogleGenerativeAI

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

# LangChain typically looks for GOOGLE_API_KEY
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Initialize the LLM
model_gemini = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1.0,  # Best practice for Gemini 3 reasoning
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
