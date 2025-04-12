import speech_recognition as sr
import pywhatkit as kit
import pyautogui
import os
import pyttsx3
import webbrowser
import time
from datetime import datetime

USER = "pawan kumar"  # Replace with your user variable or logic
music_folder = r"C:\Pawan kumar\music"
current_song_index = 0


def youtube(video):
    kit.playonyt(video)
def get_music_files(folder):
    return [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.mp3')]
music_list = get_music_files(music_folder)
def say(text):
    engine = pyttsx3.init()  # Initialize the TTS engine
    engine.say(text)  # say the text
    engine.runAndWait()
def play_music():
    global current_song_index# Check if current song index is valid
    if 0 <= current_song_index < len(music_list):
        music_path = music_list[current_song_index]
        if os.path.exists(music_path):
            os.startfile(music_path)  # This will open the music file with the default music player
            song_name = os.path.basename(music_path)  # Get the file name of the song
            say(f"Playing {song_name}")
        else:
            say("Sorry, I couldn't find the music file.")
    else:
        say("No more songs available.")
def stop_music():# Use taskkill to stop the default music player, for example, Windows Media Player
    try:         # Replace 'wmplayer.exe' with the process name of your music player
        os.system("taskkill /f /im wmplayer.exe")  # For Windows Media Player# os.system("taskkill /f /im vlc.exe")  # For VLC Player
        say("Music stopped.")
    except Exception as e:
        say("Sorry, I couldn't stop the music.")
def next_song():
    global current_song_index
    if current_song_index < len(music_list) - 1:
        current_song_index += 1
        play_music()
    else:
        say("This is the last song.")
def previous_song():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
        play_music()
    else:
        say("This is the first song.")
def click_picture_with_camera_app():
    say("Clicking the pictur sir")# Give time to make sure camera app is open
    time.sleep(2)# Simulate pressing the "Space" key (Windows Camera app uses Spacebar to capture a picture)
    pyautogui.press('space')
    say("Picture clicked.")



def say(text):
    engine = pyttsx3.init()  # Initialize the TTS engine
    engine.say(text)  # say the text
    engine.runAndWait()  # Block while processing all current speech

def pause_listening():
    global listening
    listening = False
    print("Stopped listening")

def greet_me():
    hour = datetime.now().hour
    if (hour >=6) and (hour < 12):
         say(f"Good Morning {USER}")
    elif (hour >=12) and (hour <=16):
         say(f"Good afternoon {USER}")
    elif (hour >=16) and (hour <19):
         say(f"Good evening {USER}")
    elif (hour >=19) and (hour<24):
         say(f"Good Night {USER}")
    say(f"I am JARVIS. How May I Assist you ?")



def Takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.6
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"user said: {query}")
            if 'stop listening' in query or 'exit' in query:
                hour = datetime.now().hour
                if hour >= 21 and hour < 6:
                    say("Good night sir,take care!")
                else:
                    say("Have a good day sir!")
                exit()
            return query
        except Exception as e:
            return "some error accuring. sorry for that"



if __name__ == '__main__':
    greet_me()
    while True:
        print("listening......")
        query=Takecommand()
        # sites=[["youtube","https://www.youtube.com"],["google","https://www.google.com"],["wikipedia","https://www.wikipedia.com"]]
        # for site in sites:
        #     if f"open {site[0]}".lower() in query.lower():
        #         say(f"opening {site[0]}....")
        #         webbrowser.open(site[1])
        if "how are you Jarvis" in query:
            say("I am absolutely fine sir, What about you. How May I Assist you ?")
        elif "open command prompt" in query:
            say("opening command prompt")
            os.system('start cmd')
        elif 'close command prompt' in query:
            say("Closing Command Prompt.")
            os.system("taskkill /f /im cmd.exe") 
        elif "play music" in query:
            play_music()
        elif 'next music' in query:
            next_song()
        elif 'back music' in query:
            previous_song()
        elif 'stop music' in query:
            stop_music()
        elif "current time" in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the current time is {strftime}")
            print(f"the current time {strftime}")
        elif 'current date' in query:
            current_date = datetime.now().strftime("%B %d, %Y")
            say(f"Today's date is {current_date}") 
            print(f"Today's date is {current_date}")
        elif "open camera".lower() in query.lower():
            say("opening camera sir")
            os.system("start microsoft.windows.camera:")
        elif 'click picture' in query:
            click_picture_with_camera_app()
        elif "close camera".lower() in query.lower():
            say("Closing the camera sir")
            os.system("taskkill /f /im WindowsCamera.exe") 
        elif "open YouTube" in query:
            say("What do you want to play on youtube sir?")
            video =Takecommand().lower()
            youtube(video)
            

        else:
            say("Sorry I couldn't understand. Can you please repeat that?")
        # say(text)
