import speech_recognition as sr
import webbrowser
import pyttsx3 #for text to speech

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
     if "open google" in c.lower():
         speak("opening google")
         webbrowser.open("https://google.com")
     elif "open youtube" in c.lower():
         speak("opening youtube")
         webbrowser.open("https://youtube.com")
     elif "open facebook" in c.lower():
         speak("opening facebook")
         webbrowser.open("https://facebook.com")
     elif "open linkedin" in c.lower():
         speak("opening linkedin")
         webbrowser.open("https://linkedin.com")

if __name__== "__main__":
    speak("Initializing Jarvis....")

    #Listen for the wakeing word jarvis
    #and obtain audio from the microphone
    while True:
        r=sr.Recognizer()
        
        #command
        print("recognizing.....")
        #recognise speech using sphinx


        try:
            with sr.Microphone() as source:
               print("Listening....")
               audio=r.listen(source,timeout=2,phrase_time_limit=1)
        
            command=r.recognize_google(audio)
            if(command.lower()=="jarvis"):
                speak("Yes Sir")
                #listen for command

                with sr.Microphone() as source:
                   print("Jarvis Active....")
                   audio=r.listen(source)
                   command=r.recognize_google(audio)

                   processCommand(command)
            
        
        except  Exception as e:
            print(" Error; {0}".format(e))




