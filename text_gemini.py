import base64
import os
from google import genai
from google.genai import types
import library.keys as keys
# Initialize client
client = genai.Client(api_key=keys.load_key())

# Define model and config
model = "gemini-2.0-flash"
generate_content_config = types.GenerateContentConfig(
    temperature=1,
    top_p=0.95,   
    top_k=40,
    max_output_tokens=8192,
    response_mime_type="text/plain",
    system_instruction=[
        types.Part.from_text(text="You are a helpful assistant. Motivate users to do good.")
    ],
)

# Chat history
chat_history = []

def chat():
    """
    Text based chat with Gemini API
    """
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI: Goodbye! Have a great day!")
            break

        # Append user message to history
        chat_history.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))

        # Generate response
        print("AI:", end=" ", flush=True)
        response = client.models.generate_content_stream(
            model=model,
            contents=chat_history,  # Preserve chat history
            config=generate_content_config,
        )
        
        # Read response and add to chat history
        ai_response = ""
        for chunk in response:
            print(chunk.text, end="", flush=True)
            ai_response += chunk.text

        chat_history.append(types.Content(role="model", parts=[types.Part.from_text(text=ai_response)]))

if __name__ == "__main__":
    chat()
