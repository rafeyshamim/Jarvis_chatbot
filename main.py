#Author: Mohd Rafey
#Date: 29 April 2025




import webbrowser
import pyttsx3
import client
from google import genai



ttsxEngine = pyttsx3.init()

voices = ttsxEngine.getProperty('voices')    
ttsxEngine.setProperty('voice', voices[1].id)

def speak(text):
    ttsxEngine.say(text)
    ttsxEngine.runAndWait()

def aiprocessEngine(message):
    client = genai.Client(api_key="your_api_here")

    response = client.models.generate_content(
            model="gemini-2.0-flash",
        contents = message
    )
    
    print(response.text)
    speak(response.text)


def processCommand(c):
    aiprocessEngine(c)


if __name__ == "__main__":
    speak("Initialinzing Jarvis ChatBot....")
    while True:
        word = input("give a prompt: ")

        try:
            if word =='':
                print('nothing given')
            else:
                processCommand(word)


        except ModuleNotFoundError as e:
            print(e)
        except KeyboardInterrupt as e:
            print(e)
        except ValueError as v:
            print('nothing given')


