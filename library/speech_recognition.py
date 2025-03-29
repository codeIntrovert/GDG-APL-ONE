import speech_recognition as sr

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
