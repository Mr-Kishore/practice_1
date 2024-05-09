import speech_recognition as sr
from gtts import gTTS
import os
import wikipedia

class Alan:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        #os.system("mpg321 output.mp3")  # On Linux
        os.system("start output.mp3")  # On Windows

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you repeat?")
            return ""
        except sr.RequestError as e:
            print(f"Error occurred: {e}")
            return ""

    def search_wikipedia(self, query):
        try:
            summary = wikipedia.summary(query)
            self.speak(f"Here's a summary of {query}: {summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            self.speak(f"Multiple results found for {query}. Please specify.")
        except wikipedia.exceptions.PageError:
            self.speak(f"No Wikipedia page found for {query}.")

if __name__ == "__main__":
    assistant = Alan()

    assistant.speak("Hello! I am Alan, your personal assistant. How can I assist you today?")

    while True:
        query = assistant.listen()

        if "search" in query:
            assistant.speak("What would you like to search for on Wikipedia?")
            search_query = assistant.listen()
            assistant.search_wikipedia(search_query)
        elif "exit" in query:
            assistant.speak("Exiting Alan. Goodbye!")
            break


