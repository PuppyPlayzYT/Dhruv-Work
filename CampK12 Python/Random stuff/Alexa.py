from numpy import take
import pyttsx3 as tts # python text to speech version 3
import pyjokes as jokes
import wikipedia as wiki
import pywhatkit as pwk
import speech_recognition as sr

engine = tts.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        print("Listening....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        return command

def alexa():    
    command = take_command()
    if "joke" in command:
        talk(jokes.get_joke())
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing your {song}')
        pwk.playonyt(song)
    if 'search' in command:
        search = command.replace('search', '')
        talk(wiki.summary(search, 1))


alexa()