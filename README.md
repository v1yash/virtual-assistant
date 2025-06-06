🗣️ Python Voice Assistant using Vosk
This project is a voice-controlled assistant built in Python. It uses the Vosk speech recognition library for processing voice commands and pyttsx3 for speech output. The assistant can open applications, tell the time, play music, run Python scripts, and more — all by voice.

🧠 Features
Voice recognition using Vosk

Speech output using pyttsx3

Greets based on time of day

Opens applications (e.g., Chrome, YouTube)

Plays music from a local folder

Tells the current time

Opens personal Python scripts (like a camera or Flappy Bird)

Exits on command

🧰 Technologies Used
Vosk for offline speech recognition

PyAudio for microphone input

pyttsx3 for text-to-speech

Python standard libraries: datetime, webbrowser, os

📁 Project Structure
voice_assistant/
├── README.md
├── assistant.py         # Your main Python script
├── vosk-model-en-in-0.4/ # Vosk English (India) language model
⚙️ Setup Instructions
Install Python dependencies


pip install vosk pyaudio pyttsx3
⚠ If pyaudio fails to install, use:


pip install pipwin
pipwin install pyaudio
Download the Vosk model

Download and extract the Vosk English (India) model from:
https://alphacephei.com/vosk/models
(e.g., vosk-model-small-en-in-0.4)
Then update the path in your script accordingly.

Run the assistant

Make sure your microphone is connected and run:


python assistant.py
🗂️ Supported Commands
Command	Action
"open YouTube"	Opens YouTube shortcut
"open Chrome"	Opens Google Chrome
"open videos"	Opens local Videos folder
"open StackOverflow"	Opens StackOverflow in browser
"play music" / "music"	Plays a song from local Music folder
"next" / "change"	Plays the next song
"the time"	Speaks current system time
"open code"	Opens code directory
"open camera"	Runs the camera Python script
"open PLAYit"	Opens the PLAYit media player
"flappy bird"	Runs the Flappy Bird Python game
"off" / "exit"	Quits the assistant

💡 Notes
Customize paths to match your system.

Improve Indian English command recognition by trying vosk-model-small-hi-0.22 or experimenting with larger models.

You can extend the assistant with additional commands and scripts.

🙋 Author
Yash Vaghasiya
LinkedIn
🧠 Passionate about AI and Python development
