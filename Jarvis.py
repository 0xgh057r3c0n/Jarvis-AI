from gtts import gTTS
import wikipedia
import platform
import os
import subprocess
import playsound
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from termcolor import colored
from googlesearch import search

# Function to display the colored banner
def display_banner():
    robot_art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⣶⣶⣶⣶⡄⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢠⣴⣶⣶⣶
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
    print(colored("|      Version: 1.0       |", 'yellow'))
    print(colored("|   Author: G4UR4V007     |", 'green'))
    print(colored("|                         |", 'green'))
    print(colored("===========================", 'cyan'))

# Function to convert text to speech
def speak(text):
    if text.strip():  # Check if text is not empty
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
            tts.save(f"{tmp_file.name}.mp3")
            playsound.playsound(f"{tmp_file.name}.mp3")

# Function to ask the user a question
def ask_question():
    return input("Ask me anything: ")

# Function to provide help and usage information
def show_help():
    help_text = """
    Virtual Assistant - Help Guide

    You can ask me to perform various tasks such as:
    1. Ask about the developer: "Who is your owner?"
    2. Ask about the system: "What is your operating system?"
    3. Open terminal: "Open terminal"
    4. Open browser: "Open browser"
    5. Play a song from YouTube: "Play song [song name]"
    6. Ask a question or search information: "Tell me about [topic]"
    7. Read content from a webpage aloud: "Read this webpage"
    8. Greet: "Hello", "Hi", "How are you?"

    Type 'exit', 'quit', or 'goodbye' to exit the assistant.
    """
    print(help_text)
    speak(help_text)

# Function to search for information using Google
def google_search(query):
    results = []
    try:
        for result in search(query, num_results=1):  # Use num_results for the first result
            if result.startswith("http"):  # Ensure URL is valid
                results.append(result)
                break  # Stop after getting the first valid result
    except Exception as e:
        print(f"Error during Google search: {str(e)}")
        return []
    return results

# Function to read content from a webpage
def read_webpage(url):
    driver = webdriver.Firefox()
    try:
        print(f"Visiting URL: {url}")  # Debug output
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        # Extract the main content
        content = driver.find_element(By.TAG_NAME, 'body').text
        paragraphs = content.splitlines()

        # Display and read the first two paragraphs aloud
        if len(paragraphs) > 1:
            first_paragraph = paragraphs[0]
            second_paragraph = paragraphs[1]
            print(f"First Paragraph: {first_paragraph}")
            print(f"Second Paragraph: {second_paragraph}")
            speak(first_paragraph)
            speak(second_paragraph)

            # Ask if the user wants to read more
            user_choice = input("Would you like me to read more? (yes/no): ").lower()
            if user_choice == "yes":
                for paragraph in paragraphs[2:]:
                    print(paragraph)
                    speak(paragraph)
            else:
                speak("Okay, stopping here.")
        else:
            speak("I found no relevant content to read aloud.")
    except Exception as e:
        print(f"Error reading webpage: {e}")
    finally:
        driver.quit()

# Function to fetch answers or perform tasks
def perform_task(query):
    query = query.lower()

    # Basic greetings and responses
    if "hello" in query or "hi" in query:
        return "Hello! How can I assist you today?"

    elif "how are you" in query:
        return "I'm Jarvis just a virtual assistant, but thanks for asking! How are you?"

    # Help and guidance
    elif "help" in query:
        show_help()
        return "Showing help and usage information."

    # Basic queries about the assistant and system
    elif "who is your owner" in query:
        return "I was created by Gaurav Bhattacharjee."
    elif "what is your name" in query:
        return "I am your virtual assistant."
    elif "what is your version" in query:
        return "I am version 1.0."
    elif "what is your operating system" in query:
        return f"I am running on {platform.system()} {platform.release()}."
    elif "open terminal" in query:
        if platform.system() == 'Linux':
            subprocess.run(['gnome-terminal'])
        return "Opening terminal."
    elif "open browser" in query:
        if platform.system() == 'Linux':
            subprocess.run(['xdg-open', 'https://www.google.com'])
        return "Opening your default browser."

    # Play song on YouTube
    elif "play song" in query:
        song_name = query.split("play song")[-1].strip()
        play_song(song_name)
        return f"Playing {song_name} on YouTube."

    # Search for information
    elif "tell me about" in query or "what is" in query:
        speak("Let me check Google for that.")
        google_results = google_search(query)
        
        if google_results:
            first_result = google_results[0]  # Get the first result
            read_webpage(first_result)  # Read the content of the first result
        else:
            speak("Sorry, I couldn't find any information on Google.")

    return "I don't know the answer to that yet."

# Function to play a song from YouTube
def play_song(song_name):
    speak(f"Searching for {song_name} on YouTube.")
    driver = webdriver.Firefox()  # Initialize Firefox WebDriver
    try:
        driver.get("https://www.youtube.com/results?search_query=" + song_name)
        time.sleep(2)  # Wait for the page to load

        # Click on the first video result
        first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
        first_video.click()
        time.sleep(5)  # Allow video to start

        # Skip the ad if present
        try:
            skip_button = driver.find_element(By.XPATH, '//*[@id="skip-button"]/a')
            skip_button.click()
            time.sleep(1)  # Wait for a moment after skipping
        except:
            pass  # No ad to skip

        speak(f"Now playing {song_name} on YouTube.")
    except Exception as e:
        print(f"Error during playback: {e}")
        speak("I couldn't play the song. Please check your internet connection.")
    # Removed driver.quit() to keep the window open

if __name__ == "__main__":
    display_banner()  # Display the banner
    speak("Hello! I'm Jarvis your virtual assistant, developed by Gaurav Bhattacharjee. You can ask me anything.")
    
    while True:
        try:
            question = ask_question()

            if question.lower() in ["exit", "quit", "goodbye"]:
                speak("Goodbye! Have a great day.")
                break

            response = perform_task(question)
            print(f"Answer: {response}")
            speak(response)

        except KeyboardInterrupt:
            speak("Task skipped. You can ask me anything else.")
            continue  # Skip the current task and continue asking for input

