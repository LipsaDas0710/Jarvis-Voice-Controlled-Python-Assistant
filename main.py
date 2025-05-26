import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


#recogniser is a class in sr here Im intializing the rcognizer method. 
recognizer = sr.Recognizer()
#intializing pyttsx3
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    
  


if __name__ == "__main__":    
    speak("HI I'm Jarvis")
    #Listen for the word "Jarvis"
    while True:
        import speech_recognition as sr

        # obtain audio from the microphone
        r = sr.Recognizer()
    
        print("recognising....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                audio = r.listen(source , timeout=2, phrase_time_limit=3)
                print("Listening...")
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yeah")
            #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis is active...")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)
            
        # except sr.UnknownValueError:
        #     print("Could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))