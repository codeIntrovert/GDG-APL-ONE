import speech_recognition as sr
from google import genai
from google.genai import types
import library.keys as keys
from library.lib_functions import speak
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

# Initialize speech recognition
recognizer = sr.Recognizer()



def listen():
    """
    Uses Google Cloud regonition + gemini
    alexa prototype
    Uses pyttsx3 for text to speech
    """
    with sr.Microphone() as source:
        print("\nListening...")
        #recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, phrase_time_limit=30)
            text = recognizer.recognize_google(audio, language='en-US')
            print("You:", text)
            return text
        except sr.UnknownValueError:
            print("Couldn't understand, please repeat...")
            return None
        except sr.RequestError:
            print("Speech recognition error, check internet connection.")
            return None

def chat():
    while True:
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
