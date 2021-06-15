import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
switch = 0

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try :
        with sr.Microphone() as source:
            print('listening...........')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'shinchan' in command:
                command = command.replace('shinchan','')
                print(command)
    except:
        pass 
    return command

def run_shinchan():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time s'+time)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'care'in command:
        talk('bye!Have a nice day')
        print('bye!Have a nice day')

    elif 'who' in command:
        person = command.replace('who','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'clean'in command:
        talk('please wait, It will be done')
        print('please wait, It will be done')

    elif 'hello'in command:
        talk('Hello,How are you')
        print('Hello,How are you')

    elif 'how are you'in command:
        talk('I am good, How can I help you!')
        print('I am good, How can I help you!')

    else:
        talk('please say again')

while True:
    run_shinchan()

     