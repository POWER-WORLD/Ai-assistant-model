import speech_recognition as sr
import pyttsx3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except Exception as e:
            print("Sorry, I didn't catch that.")
            return "None"
        return query.lower()

# Selenium WebDriver to open YouTube and search for a video
driver = None

def open_youtube(video):
    global driver
    say(f"Opening YouTube and searching for {video}")
    
    # Specify the path to your ChromeDriver or ensure it's in your system PATH
    driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
    
    # Open YouTube and search for the video
    driver.get(f"https://www.youtube.com/results?search_query={video}")
    time.sleep(5)  # Let the YouTube page load

def close_youtube_tab():
    global driver
    if driver:
        say("Closing the YouTube tab.")
        driver.close()  # This will close the current YouTube tab
        driver = None
    else:
        say("No YouTube tab is currently open.")

if __name__ == "__main__":
    say("Say 'open YouTube' to play a video or 'close YouTube' to close the tab.")
    while True:
        query = take_command()

        if 'open youtube' in query:
            say("What do you want to play on YouTube, sir?")
            video = take_command().lower()
            if video != "none":
                open_youtube(video)
        
        elif 'close youtube' in query or 'close tab' in query:
            close_youtube_tab()

        # Stop the loop when 'exit' or 'stop' is said
        if 'exit' in query or 'stop' in query:
            say("Goodbye!")
            break


