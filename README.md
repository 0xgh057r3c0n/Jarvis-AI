# Jarvis Voice Assistant 2.0

![Jarvis](https://img.shields.io/badge/AI%20Assistant-Jarvis%202.0-red)  
🎤 A voice-controlled assistant using Google Gemini, Speech Recognition, and Selenium automation.

## 🔧 Features

- Voice-activated assistant
- Natural language responses via Gemini 2.0 API
- Google search and webpage reading
- YouTube music playback with ad skipping
- System info, terminal/browser launching
- Personalized TTS (Text-to-Speech) via gTTS

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
````

Contents of `requirements.txt`:

```
SpeechRecognition
gTTS
playsound
selenium
termcolor
googlesearch-python
requests
```

### 🦎 GeckoDriver Setup (for Firefox)

1. **Download GeckoDriver**:

   * Go to: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
   * Choose your OS version, extract the binary.

2. **Add to PATH**:

   * **Linux/macOS**:

     ```bash
     sudo mv geckodriver /usr/local/bin/
     chmod +x /usr/local/bin/geckodriver
     ```
   * **Windows**:
     Add the folder containing `geckodriver.exe` to the system PATH.

3. **Ensure Firefox is installed**.

---

## ▶️ Running Jarvis

```bash
python Jarvis.py
```

Jarvis will greet you with a voice prompt.

## 🗣️ Voice Commands Supported

* `Play song [song name]`
* `What is...`, `Who is...`, `Define...`
* `Tell me about [topic]`
* `Open terminal`, `Open browser`
* `What is your version`, `What is your name`
* `Exit`, `Quit`, `Goodbye`

---

## 💡 Example Session

```
🎤 Listening...
You: What is artificial intelligence?
Jarvis: Artificial intelligence is the simulation of human intelligence in machines...
🎤 Listening...
You: Play song Shape of You
Jarvis: Playing Shape of You on YouTube.
```

---

## 🧠 Powered By

* **Google Gemini API (2.0 Flash)**
* **SpeechRecognition (Google recognizer)**
* **Selenium with Firefox**
* **gTTS (Google Text-to-Speech)**

---

## 👨‍💻 Author

**Gaurav Bhattacharjee (0xgh057r3c0n)**

---
