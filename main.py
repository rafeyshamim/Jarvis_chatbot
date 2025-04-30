# Author: Mohd Rafey Shamim Khan
# Date: 29 April 2025

# Import necessary modules
import webbrowser              # Used for opening URLs (currently unused in this script)
import pyttsx3                 # Text-to-speech conversion library
import client                  # User-defined module to initialize the Gemini client
from google import genai       # Google's Gemini generative AI library

# Initialize the TTS engine
ttsxEngine = pyttsx3.init()

# Set the voice to a preferred voice (typically female)
voices = ttsxEngine.getProperty('voices')    # Get available system voices
ttsxEngine.setProperty('voice', voices[1].id) # Set desired voice (change index if needed)

# Speak a given string out loud
def speak(text):
    ttsxEngine.say(text)
    ttsxEngine.runAndWait()

# Process input through Gemini API and speak the result
def aiprocessEngine(message):
    # Initialize the Gemini client with API key (replace 'your_api_here' with your actual API key)
    client = genai.Client(api_key="your_api_here")

    # Generate a response using Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message
    )

    # Output and speak the response
    print(response.text)
    speak(response.text)

# Process user command (send it to Gemini)
def processCommand(c):
    aiprocessEngine(c)

# Entry point of the script
if __name__ == "__main__":
    speak("Initializing Jarvis ChatBot....")

    # Run an infinite loop to accept user prompts
    while True:
        word = input("Give a prompt: ")

        try:
            if word == '':
                print('Nothing given')
            else:
                processCommand(word)

        # Handle common exceptions
        except ModuleNotFoundError as e:
            print("Module not found:", e)
        except KeyboardInterrupt as e:
            print("Interrupted by user:", e)
        except ValueError as v:
            print("Invalid input:", v)
