import os
from ai_speech import speak
#to search, will ask search query at the time of execution




def music():
    print("Now Playing... My Ordinary Life")
    led = "C:\\Users\\Hasan Imam\\Music\\My Ordinary Life-The Living Tombstone-9Zj0JOHJR-s.m4a"
    os.startfile(led)
    return


def open_application(query):
    if "browser" in query:
        speak("Opening Microsoft Edge")
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
        return
    elif "code" in query:
        speak("Opening Visual Studio")
        os.startfile('"C:\\Users\\Hasan Imam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
        return
    elif "spotify" in query:
        speak("Spotify")
        os.startfile("C:\\Users\\Hasan Imam\\Desktop\\Spotify.lnk")
        return
    else:
        speak("Application not available")
        return