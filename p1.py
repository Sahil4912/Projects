import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import AppOpener
import os
#import smtplib      "This module is use to send mail through email"



dict = {1:"Sahil", 2:"Sai", 3:"Azad", 4:"Tanishq", 5:"Dhanraj"}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, how can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print("User said = ", query,"\n")
    
    except Exception as e:
        #print(e)
        print("Say that again please...") 
        return "None"
    return query
    
'''    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.start("Youremail@gmail.com", "your-password")
        server.send('youremail@gmail.com', to, content)
        server.close()'''
    
    
if __name__ =="__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia.......')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open word' in query:
            AppOpener.open("word")
        
        #elif 'play music' in query:
        #    os

        elif 'open code' in query:
            AppOpener.open("Visual Studio Code")

        elif 'open setting' in query:
            AppOpener.open("Settings")

        elif 'open calculator' in query:
            AppOpener.open("calculator")

        elif 'file explorer' in query:
            AppOpener.open("file explorer")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        '''elif 'send mail to sahil' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "mansinghpawar1@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")  
            except Exception as e:
                speak("I am not able to send this email")'''


        


    #speak("Sahil is a good boy")