import platform
import os
import subprocess
import tempfile
import time
import requests
import speech_recognition as sr
from gtts import gTTS
import playsound
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from googlesearch import search
import contextlib
import sys

# Gemini API Setup
GEMINI_API_KEY = "AIzaSyAJiKNprgDXWiyHggCvL9qcwg0XYyEgPYs"
GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
HEADERS = {"Content-Type": "application/json"}

def display_banner():
    robot_art = """
            ⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
            ⣶⣶⣶⣶⡄⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢠⣴⣶⣶⣶
            ⢹⣿⡿⣿⣷⠀⠿⣿⣿⣿⣦⣀⠀⠀⠀⠀⣀⣴⣿⣿⣿⠿⠀⣾⣿⢿⣿⡏
            ⠘⣿⣷⣬⡙⠿⣦⣌⡙⠿⣿⣿⣷⣦⣴⣾⣿⣿⠿⢋⣡⣴⠿⣿⣯⣿⣿⠃
            ⠀⢻⣿⣌⠛⢷⣌⡙⢿⣶⡌⠙⢿⣿⣿⠿⠋⢡⣶⡿⢋⣡⡶⠛⣡⣿⡟⠀
            ⠀⠘⠿⣿⣿⣦⣌⠛⢾⣿⣇⠸⣷⣌⣡⣶⡇⣸⣿⡷⠛⣡⣴⣿⣿⠿⠃⠀
            ⠀⠀⢠⣌⠻⢿⣿⣿⣦⣿⣿⠀⣿⣿⣿⣿⠀⣿⣿⣴⣿⣿⡿⠟⣡⡄⠀⠀
            ⠀⠀⢸⣿⣷⠀⠀⠉⠉⠉⠛⠀⣿⣿⣿⣿⠀⠛⠉⠉⠉⠀⠀⣾⣿⡇⠀⠀
            ⠀⠀⢸⣿⣿⣿⣦⠀⢠⣴⣾⡇⢸⣿⣿⣿⠀⣷⣦⡄⠀⣴⣿⣿⣿⡇⠀⠀
            ⠀⠀⠀⣿⣿⣿⣿⠀⢸⣿⣿⡇⢸⣿⣿⣿⠀⣿⣿⡇⠀⣿⣿⣿⣿⠁⠀⠀
            ⠀⠀⠀⣿⣿⣿⣿⠀⢸⣿⣿⡇⢾⣿⣿⣿⠀⣿⣿⡇⠀⣿⣿⣿⣿⠀⠀⠀
            ⠀⠀⠀⠻⢿⣿⣿⠀⢸⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⡇⠀⣿⣿⣿⠟⠀⠀⠀
            ⠀⠀⠀⠀⠀⠙⢿⠀⢸⣿⣿⠋⣉⣉⣉⣉⠉⣿⣿⡇⠀⡿⠋⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠃⣼⣿⣿⣿⣿⣧⠘⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠛⠛⠛⠛⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print(colored(robot_art, 'red'))
    print(colored("===========================", 'cyan'))
    print(colored("|    Virtual Assistant    |", 'cyan'))
    print(colored("|      Version: 2.0       |", 'yellow'))
    print(colored("|   Author: 0xgh057r3c0n  |", 'green'))
    print(colored("===========================", 'cyan'))

def speak(text):
    if text.strip():
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts.save(tmp_file.name)
            with open(os.devnull, 'w') as fnull, contextlib.redirect_stderr(fnull):
                playsound.playsound(tmp_file.name)
            os.remove(tmp_file.name)

def ask_question():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            with contextlib.redirect_stderr(open(os.devnull, 'w')):
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            query = recognizer.recognize_google(audio)
            print(f"You: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""

def normalize(text):
    return text.strip().lower()

def ask_gemini(prompt):
    try:
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        res = requests.post(GEMINI_API_URL, headers=HEADERS, json=payload)
        res.raise_for_status()
        return res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        return f"Gemini error: {e}"

def google_search(query):
    try:
        return next(search(query, num_results=1))
    except:
        return None

def read_webpage(url):
    options = Options()
    options.set_preference("log.level", "3")
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url)
        time.sleep(3)
        content = driver.find_element(By.TAG_NAME, "body").text
        for p in content.splitlines():
            if len(p.strip().split()) > 5:
                print(p)
                speak(p)
    finally:
        driver.quit()

def play_song(song_name):
    speak(f"Playing {song_name} on YouTube.")
    options = Options()
    options.set_preference("media.autoplay.default", 0)
    options.set_preference("media.autoplay.blocking_policy", 0)
    options.set_preference("media.autoplay.allow-extension-background-pages", True)
    options.set_preference("log.level", "3")

    driver = webdriver.Firefox(options=options)

    try:
        driver.get(f"https://www.youtube.com/results?search_query={song_name}")
        time.sleep(3)
        video = driver.find_element(By.ID, "video-title")
        video_url = video.get_attribute("href")
        driver.get(video_url + "&autoplay=1")
        time.sleep(5)
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
        driver.execute_script("document.querySelector('video').play()")

        speak("Checking for ads...")
        ad_skipped = False
        for _ in range(15):
            try:
                skip_button = driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button")
                speak("Ad is playing... Skipping now.")
                skip_button.click()
                ad_skipped = True
                speak("Ad skipped.")
                break
            except NoSuchElementException:
                time.sleep(1)
        if not ad_skipped:
            speak("Ad ended or could not be skipped.")

        driver.find_element(By.TAG_NAME, "body").send_keys("f")
        time.sleep(1)
        driver.execute_script("document.querySelector('video').play()")
        speak("Playing now. Press Enter to stop.")
        input("🎵 Press Enter to close the browser and stop music...")

    except Exception as e:
        speak(f"Error playing song: {e}")
    finally:
        driver.quit()
    return "Done"

def show_help():
    help_text = """
    You can ask me to:
    - Play a song: 'Play song [song name]'
    - Ask anything: 'What is...', 'Who is...'
    - Get system info: 'What is your operating system'
    - Open apps: 'Open terminal', 'Open browser'
    - Know me: 'What is your name', 'Who is your owner'
    - Quit: 'Exit', 'Quit', 'Goodbye'
    """
    print(help_text)
    speak(help_text)

def perform_task(query):
    query = normalize(query)

    if query in ["hi", "hello"]:
        speak("Hello! How can I help you today?")
        return

    elif query in ["exit", "quit", "goodbye"]:
        speak("Goodbye! Have a great day.")
        exit()

    elif "help" in query:
        show_help()
        return

    elif any(kw in query for kw in ["your name", "tell me your name", "say your name", "identify yourself", "give me your name", "name yourself", "whats your name", "who are you"]):
        speak("I am your virtual assistant.")
        return

    elif any(kw in query for kw in ["your version", "which version", "say your version", "version are you", "give me your version", "share your version", "what version are you"]):
        speak("I am version 1.1.")
        return

    elif any(kw in query for kw in ["your operating system", "which os", "say your os", "tell me your os", "give me your system info", "share your platform", "whats your os"]):
        speak(f"I am running on {platform.system()} {platform.release()}.")
        return

    elif any(kw in query for kw in ["who is your owner", "your creator", "who made you", "who built you"]):
        speak("I was created by Gaurav Bhattacharjee.")
        return

    elif "open terminal" in query:
        if platform.system() == 'Linux':
            subprocess.run(['gnome-terminal'])
        speak("Opening terminal.")
        return

    elif "open browser" in query:
        if platform.system() == 'Linux':
            subprocess.run(['xdg-open', 'https://www.google.com'])
        speak("Opening your default browser.")
        return

    elif "play song" in query:
        song = query.replace("play song", "").strip()
        play_song(song)
        return

    elif query.startswith("what is") or query.startswith("who is") or query.startswith("define"):
        speak("Ok wait let me think.")
        # Ask Gemini for a short, plain-language answer
        short_query = f"{query}. Answer briefly in one or two simple sentences, no bullet points, no code, no formatting."
        answer = ask_gemini(short_query)

        # Ensure no weird formatting slips through
        clean_answer = answer.replace("**", "").replace("*", "").strip()

        print(f"Jarvis: {clean_answer}")
        speak(clean_answer)
        return

    elif "tell me about" in query:
        speak("Let me check Google.")
        url = google_search(query)
        if url:
            read_webpage(url)
        else:
            speak("No information found.")
        return

    speak("Ok wait let me think.")
    answer = ask_gemini(query)
    print(f"Jarvis: {answer}")
    speak(answer)

if __name__ == "__main__":
    display_banner()
    speak("Hello! I'm Jarvis, your assistant developed by Gaurav Bhattacharjee. Ask me anything.")
    while True:
        try:
            question = ask_question()
            if question.strip():
                perform_task(question)
        except KeyboardInterrupt:
            speak("Interrupted. You may ask something else.")
