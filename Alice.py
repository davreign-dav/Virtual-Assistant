import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import ecapture as ec
import time
import subprocess
import wolframalpha
import urllib.parse
import requests
chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello Sir,Good Morning")
        print("Hello Sir,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello Sir,Good Afternoon")
        print("Hello Sir,Good Afternoon")
    else:
        speak("Hello Sir,Good Evening")
        print("Hello Sir,Good Evening")

def tellDay():
      
  
    day = datetime.datetime.today().weekday() + 1
    
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print("The day is ",day_of_the_week)
        speak("The day is " + day_of_the_week)

  
def tellTime():
    
    time = str(datetime.datetime.now())
    
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")
    

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"You said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again.")
            return "None"
        return statement

wishMe()

print('I am Alice, your basic model virtual assistant.')
speak("I am Alice, your basic model virtual assistant.")



if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?.")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak('your personal assistant Alice is shutting down,Good bye Sir')
            print('your personal assistant Alice is shutting down,Good bye Sir')
            break

        if "from wikipedia" in statement:
              
            speak("Checking the wikipedia ")
            query = statement.replace("wikipedia"," ")              
    
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(result)
            speak(result)
            

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="37ad0f5bd38d157032013c7dc869f3c1"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            print('I am Alice version 1.o a personal assistant created by Devendra or say David. I am programmed to execute minor tasks like'
                  'opening youtube,google chrome,gmail ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me some computational questions too!. I am happy to help you.')
            speak('I am Alice version 1.o a personal assistant created by Devendra or say David. I am programmed to execute minor tasks like'
                  'opening youtube,google chrome,gmail ,predict time,take a photo,search wikipedia,predict weather.' 
                  'in different cities , get top headline news from times of india and you can ask me some computational questions too!. I am happy to help you.')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I have been created by Devendra SIngh Chauhan or say David.")
            print("I have been created by Devendra SIngh Chauhan or say David.")

        elif "will you be my gf" in statement or "will you be my bf" in statement:  
            speak("I'm not sure about, may be you should give me some time")


        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.ecapture(0,"Alice camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            url = "https://www.google.com.tr/search?q=".format(statement)    
            webbrowser.get(chromedir).open_new_tab(url)
            time.sleep(5)

        elif 'play' in statement:
            song=statement.replace('play','')
            speak("playing " + song)
            pywhatkit.playonyt(song)
            
        
        elif "which day it is" in statement:
            tellDay()
            continue
          
        elif "tell me the time" in statement:   
            tellTime()
            continue

        elif 'do some maths' in statement or 'try some calculation' in statement or 'try some computtaional' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="E8X2QV-7T757T32XA"
            client = wolframalpha.Client('E8X2QV-7T757T32XA')
            res = client.query(question)
            answer = next(res.results).text
            print("Your answer is:" +answer)
            speak("Your answer is:" + answer)
            

        


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "shutdown" in statement:
            speak("Ok , your pc will shutdown in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/s"])

        elif "restart" in statement:
            speak("Ok , your pc will restart in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/r"])
time.sleep(0)

