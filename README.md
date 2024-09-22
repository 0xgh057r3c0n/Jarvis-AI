# Jarvis-AI Python3 Virtual Assistant

## Overview

**Jarvis-AI** is a Python-based virtual assistant capable of performing various tasks such as searching for information, reading webpage content, playing songs on YouTube, and responding to user inquiries. The assistant uses voice interaction for user engagement and is primarily designed for Linux systems.

---

## Features

1. **Text-to-Speech**: Converts text to speech using the `gTTS` (Google Text-to-Speech) module.
2. **Google Search**: Uses `googlesearch` to fetch information from the web.
3. **Webpage Reading**: Reads content from a webpage using Selenium and converts it to speech.
4. **System Information**: Provides system information like the operating system version.
5. **Open Applications**: Can open a terminal or default browser (Linux environment).
6. **YouTube Music Playback**: Plays songs on YouTube by searching and interacting with the webpage.
7. **Interactive Help**: Offers a guide on how to interact with Jarvis through text or speech commands.

---

## Dependencies

To use **Jarvis-AI**, you need to install the following Python packages:

```bash
pip install gtts wikipedia selenium playsound termcolor googlesearch-python
```

### Additional Requirements

- **Web Drivers**: Selenium requires web drivers to control browsers. You can use either Chrome or Firefox drivers.
  - Download [Firefox geckodriver](https://github.com/mozilla/geckodriver/releases) or [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).
  
- **Audio Playback**: Ensure your system has an audio setup. `playsound` library is used for playing TTS output.

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/0xgh057r3c0n/jarvis-AI.git
   ```

2. **Run the Script**:

   ```bash
   python3 Jarvis.py
   ```

---


### Expected Terminal Output:

```bash
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⣶⣶⣶⣶⡄⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢠⣴⣶⣶⣶
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

===========================
|    Virtual Assistant    |
|       Version: 1.0      |
|  Developed by Gaurav    |
|   Bhattacharjee         |
===========================
```

After the banner is displayed, the assistant will start with a welcome message and await your input:

```bash
Hello! I'm your virtual assistant, developed by Gaurav Bhattacharjee. You can ask me anything.
Ask me anything: 
```

---

### Interaction Example:

**User Input**:
```bash
Ask me anything: Hello
```

**Output**:
```bash
Answer: Hello! How can I assist you today?
```

## Usage

After running the script, you'll see an introductory banner with developer details. You can then interact with Jarvis via voice or text commands. Here are some example commands:

- **General Questions**: "Tell me about Python."
- **System Info**: "What is your operating system?"
- **Open Terminal/Browser**: "Open terminal" or "Open browser."
- **Play Music**: "Play song [song name]."
- **Help**: "Help."

To exit, use `exit`, `quit`, or `goodbye`.

---

## Functions

1. **`display_banner()`**: Displays an ASCII art banner with version info.
2. **`speak(text)`**: Converts text to speech using the `gTTS` module.
3. **`ask_question()`**: Prompts the user for input.
4. **`show_help()`**: Displays a help guide for interacting with the assistant.
5. **`google_search(query)`**: Performs a Google search using `googlesearch`.
6. **`read_webpage(url)`**: Fetches and reads aloud content from a webpage using Selenium.
7. **`perform_task(query)`**: Main logic to handle user commands and queries.
8. **`play_song(song_name)`**: Searches YouTube for a song and plays it using Selenium.

---

## Example Commands

1. **Greeting**:
   - **Command**: "Hello"
   - **Response**: "Hello! How can I assist you today?"

2. **Ask About the Developer**:
   - **Command**: "Who is your owner?"
   - **Response**: "I was created by Gaurav Bhattacharjee."

3. **Get System Information**:
   - **Command**: "What is your operating system?"
   - **Response**: "I am running on [Operating System]."

4. **Play a Song**:
   - **Command**: "Play song Bohemian Rhapsody"
   - **Response**: "Playing Bohemian Rhapsody on YouTube."

5. **Search for Information**:
   - **Command**: "Tell me about machine learning."
   - **Response**: Performs Google search and reads the result.

---

## License

This project is licensed under the GNU General Public License v3.0. You can redistribute and modify the software under the terms of the GPL license.

### GPL-3.0 License Summary

- **Freedom to Use**: You are free to use this software for any purpose.
- **Freedom to Modify**: You can modify the software to suit your needs.
- **Freedom to Share**: You can distribute copies of the software.
- **Freedom to Contribute**: You can contribute changes back to the community.
- **Copyleft**: Any modifications or derived works must also be licensed under GPL-3.0, ensuring freedom for all users.

For more information, read the full [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html).

---

## Contribution

Feel free to fork the project, submit issues, and create pull requests. Contributions are welcome!

---

## Developer

- **Gaurav Bhattacharjee**

This assistant provides an engaging and interactive way to interact with your system using voice commands and web automation. Explore its capabilities and customize it to fit your needs!
