import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
#import openai
import webbrowser
import subprocess as sp
import smtplib
import playsound
#import pywhatkit
#from twilio.rest import Client
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[32].id)
#openai.api_key = "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"
'''def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def news(me):
    # the target we want to open
    url = 'https://www.merriam-webster.com/dictionary/' + me
    webbrowser.open_new(url)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('achjai457@gmail.com', 'abcdef@123')
    server.sendmail("achjai457@gmail.com", to, content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning achintya! I am Genie! How may I help You?")
    elif 12 <= hour < 17:
        speak("Good Afternoon achintya! I am Genie! How may I help You?")
    else:
        speak("Good Evening achintya! I am Genie! How may I help You?")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 150
        r.non_speaking_duration = 0.5
        audio = r.listen(source)
    try:
        print("okay, WIP")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print("User said: ", query)  # User query will be printed.
    except Exception as e:
        # print(e)
        speak("Please Say that again...")  # Say that again will be printed in case of improper voice
        # exit()
        return "None"  # None string will be returned
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'tell me about' in query:
            # Converting user query into lower case
            # Logic for executing tasks based on query
            # if wikipedia found in the query then this block will be executed
            query = query.replace("tell me about ", "")
            speak('Searching' + query)
            results = wikipedia.summary(query, sentences=2)
            speak("Here's what I found on wikipedia")
            webbrowser.open_new("https://en.wikipedia.org/wiki/" + query)
            speak(results)
        elif 'what is the meaning of' in query:
            me = query.replace("what is the meaning of ", "")
            news(me)
        elif 'search' in query:
            se = query.replace("search ", "")
            pywhatkit.search(se)
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        elif 'email' in query:
            try:
                speak("Please Enter the email (I D)")
                to = input("Enter Email.: ")
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent to " + to + "(I D) successfully!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
        elif 'play song' in query:
            speak("Which songs should I play?")
            song = takeCommand()
            webbrowser.open_new("https://www.youtube.com/results?search_query=" + song)
            speak("Please select the first item to play the song")
        elif 'show' in query:
            se = query.replace("show ", "")
        elif 'open' in query:
            try:
                app = query.replace("open ", "")
                path = '/Applications/' + app[0].upper() + app[1:len(app)] + ".app"
                sp.call(['open', path])
            except Exception as e:
                # print(e)
                speak("Sorry my friend, There is no app in this system")
        elif 'send whatsapp message' in query:
            speak("Please enter the no. to send the message")
            num = input("Enter No.: ")
            speak("Please say the message loud and clear")
            msg = takeCommand()
            #c = Client("AC9141be76481b0c6d17167829888f1caa", "704475cdb5eede155c1edfb761caa8b1")
            c.messages.create(body=msg, from_='whatsapp:+19257255530', to = num)
            speak("The Message is Delivered successfully!")
        elif 'look gmail' in query:
            webbrowser.open_new("https://gmail.com")
        elif 'look meet' in query:
            webbrowser.open_new("https://meet.google.com")
        elif 'look class' in query:
            webbrowser.open_new("https://classroom.google.com")
        elif 'look youtube' in query:
            webbrowser.open_new("https://youtube.com")
        elif 'look google' in query:
            webbrowser.open_new("https://google.com")
        elif 'look stackoverflow' in query:
            webbrowser.open_new("https://stackoverflow.com")
        elif 'look colab' in query:
            webbrowser.open_new("https://colab.research.google.com")
        elif 'look at my dad\'s website' in query:
            webbrowser.open_new("https://www.adityajaimini.com")
        elif 'hello' in query:
            speak("Hello There...")
        elif 'how are you' in query:
            speak("I Am Great, Thanks For Asking...")
        elif 'who are you' in query:
            speak("I am Your Genie! A genie with unlimited wishes")
        elif 'who made you' in query:
            speak("I Was Made By Achintya And Gauransh. They Both Are Genius")
        elif 'what can you do' in query:
            app = '/Users/achintyajaimini/Documents/music/Voice.mp3'
            playsound.playsound(app)
        elif 'bye' in query:
            speak("bye bye, see you soon")
            exit()
        elif 'thank you' in query:
            speak("Your Welcome")
            exit()
        elif 'get out' in query:
            speak("Ok")
            exit()
        
