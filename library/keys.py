import os
from dotenv import load_dotenv

def load_key():
    """Load the API key from an environment variable."""
    # Load environment variables from .env
    load_dotenv()
    # Access the API key
    api_key = os.getenv("API_KEY")
    if api_key is None:
        raise ValueError("API key not found. Please set the API_KEY environment variable.")
    return api_key