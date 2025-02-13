from vosk import Model, KaldiRecognizer
import pyaudio
import os
import pyttsx3 
import datetime
import webbrowser

# ...........................................
query=""
a=0
# function's.................................

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning yash!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon yash!")   

    else:
        speak("Good Evening yash!")  

    speak("I am A B. Please tell me how may I help you")
    # speak("ok")

# vosk-model-small-en-in-0.4
# vosk-model-small-hi-0.22

# logical work's..........................................
model =Model(r"C:/Users/vagha/OneDrive/Documents/AI/vosk/vosk-model-en-in-0.4")
recognizer = KaldiRecognizer(model,16000)


mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1,rate=16000,input=True,frames_per_buffer=8192)
stream.start_stream()


wishMe()
while True:
    data = stream.read(8192)
    if recognizer.AcceptWaveform(data):
        # print(recognizer.Result())
        query = recognizer.Result() 
        print(query)

# command's....................................................

        if 'open you tube' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Desktop\\YouTube.lnk"
            os.startfile(codePath)

        elif 'open youtube' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Desktop\\YouTube.lnk"
            os.startfile(codePath)
            
        elif 'youtube' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Desktop\\YouTube.lnk"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(codePath)    

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open videos' in query:
            codePath = "C:\\Users\\vagha\Videos"
            os.startfile(codePath)
            
        elif 'open video' in query:
            codePath = "C:\\Users\\vagha\Videos"
            os.startfile(codePath)

        elif 'video' in query:
            codePath = "C:\\Users\\vagha\Videos"
            os.startfile(codePath)
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\vagha\\Music'
        
        elif 'music' in query:
            music_dir = 'C:\\Users\\vagha\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[a]))

        elif 'change' in query:
            a=a+1
            music_dir = 'C:\\Users\\vagha\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[a]))
            
        elif 'next' in query:
            a=a+1
            music_dir = 'C:\\Users\\vagha\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[a]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
             
        elif 'open google chrome' in query:
            codePath = "C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(codePath)
        
        elif 'open code' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Documents\\AI"
            os.startfile(codePath)
        
        elif 'open camera' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Documents\\AI\\camera.py"
            os.startfile(codePath)
        
        elif 'camera' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Documents\\AI\\camera.py"
            os.startfile(codePath)

        elif 'open play it' in query:
             codePath = "C:\\Users\\vagha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\PLAYit\\PLAYit.lnk"
             os.startfile(codePath) 

        elif 'open playit' in query:
            codePath = "C:\\Users\\vagha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\PLAYit\\PLAYit.lnk"
            os.startfile(codePath) 

        elif 'flappy bird' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Documents\\AI\\flappy bird.py"
            os.startfile(codePath)
            
        elif 'flapy' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Documents\\AI\\flappy bird.py"
            os.startfile(codePath)    
          
       
       
        # elif 'email to yash' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "vaghasiyayash2607@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend yash. I am not able to send this email")  

        elif 'off' in query:
            quit()

        elif 'exit' in query:
            quit()    

        else:
            print("No query matched")


