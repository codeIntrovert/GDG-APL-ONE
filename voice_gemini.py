from google import genai
from google.genai import types
import library.keys as keys
from library.ai_speech import speak
from library.speech_recognition import listen
from library.lib_functions import *
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
        types.Part.from_text(text="You are a helpful assistant, keep responses short and under 100 words. text only responses are preferred. Do not include any code snippets or markdown. Do not include any links or URLs. Do not include any emojis. Do not include any special characters. Do not include any numbers."),
    ],
)

chat_history = []

def chat():
    while True:
        user_input = listen() # Get user input from speech recognition
        if not user_input:
            continue

        user_input = user_input.lower()

        if user_input in ["exit", "quit", "bye"]:
            print("AI: Goodbye! Have a great day!")
            speak("Goodbye! Have a great day!")
            break

        elif "youtube" in user_input:
            open_youtube()
        elif "music" in user_input or "spotify" in user_input:
            open_spotify()
        # elif "search for" in user_input:
        #     query = user_input.replace("search for", "").strip()
        #     google_search(query)
        elif "weather" in user_input:
            weather_report = get_weather()
            print("AI:", weather_report)
            speak(weather_report)
        elif "shutdown" in user_input or "restart" in user_input:
            control_system(user_input)


        else:
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
