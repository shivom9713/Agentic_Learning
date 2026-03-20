from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
import yfinance as yf

search_tool = DuckDuckGoSearchRun()


@tool
def calculate (a: int, b: int, operation: str) -> int:
    """Can perform calculations. Takes two integers as input and returns multiplication, division, addition, and subtraction of the two numbers.
    use 'add' for addition, 'subtract' for subtraction, 'multiply' for multiplication, and 'divide' for division."""
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b   
    except Exception as e:
        return f"Error performing calculation: {str(e)}"
    




@tool
def get_stock_price(symbol: str) -> str:
    """Get current stock price for a given ticker symbol (e.g., AAPL, TSLA)."""
    
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        
        if data.empty:
            return f"No data found for {symbol}"
        
        price = data["Close"].iloc[0]
        
        return data.to_string()
    
    except Exception as e:
        return f"Error fetching stock price: {str(e)}"