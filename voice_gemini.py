from google import genai
from google.genai import types
import library.keys as keys
from library.lib_functions import speak
from library.lib_functions import listen
# Initialize Google Gemini API
client = genai.Client(api_key=keys.load_key())
model_name = "gemini-2.0-flash"

generate_content_config = types.GenerateContentConfig(
    temperature=1,
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192,
    response_mime_type="text/plain",
    system_instruction=[
        types.Part.from_text(text="You are a helpful assistant, similar to ironman's jarvis")
    ],
)

chat_history = []

def chat():
    while True:
        #user_input = input("\nYou: ")
        user_input = listen()
        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI: Goodbye! Have a great day!")
            speak("Goodbye! Have a great day!")
            break

        chat_history.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))

        print("AI:", end=" ", flush=True)
        ai_response = ""
        
        for chunk in client.models.generate_content_stream(
            model=model_name, contents=chat_history, config=generate_content_config
        ):
            print(chunk.text, end="", flush=True)
            ai_response += chunk.text

        print("\n")
        speak(ai_response)
        chat_history.append(types.Content(role="model", parts=[types.Part.from_text(text=ai_response)]))

if __name__ == "__main__":
    chat()
