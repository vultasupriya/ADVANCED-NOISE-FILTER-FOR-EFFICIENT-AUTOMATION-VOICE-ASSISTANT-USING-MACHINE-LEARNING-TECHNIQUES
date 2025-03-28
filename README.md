# ADVANCED NOISE FILTER FOR EFFICIENT AUTOMATION VOICE ASSISTANT USING MACHINE LEARNING TECHNIQUES

## Description
This project implements a voice assistant with both command-line and GUI interfaces. The primary focus is on **noise reduction** to enhance speech recognition accuracy. The assistant can perform various tasks such as web searches, YouTube queries, telling jokes, providing weather updates, and reading news.

## Features
- **Advanced noise reduction** for improved speech clarity
- Speech recognition
- Web search using Selenium
- YouTube searches
- Read the latest news
- Tell jokes
- Provide weather updates
- Text-to-speech functionality

## Installation
### Prerequisites
Ensure you have Python installed and install the required dependencies using:

```sh
pip install speechrecognition selenium beautifulsoup4 gtts playsound numpy noisereduce matplotlib opencv-python tk
```

## Usage
### 1. Running the Command-Line Version
Execute the following command to run the voice assistant without a GUI:
```sh
jupyter notebook major.ipynb
```
Run all cells in sequence.

### 2. Running the GUI Version
Execute the following command to launch the GUI-based assistant:
```sh
jupyter notebook major_gui.ipynb
```
Run all cells in sequence.

## Noise Reduction Implementation
- Uses **noisereduce** library to filter out background noise from audio inputs.
- Converts audio to NumPy arrays for processing.
- Enhances the accuracy of speech recognition by reducing unwanted sounds.

## Dependencies
- Python
- OpenCV
- NumPy
- Tkinter (for GUI version)
- SpeechRecognition
- Selenium (for web search)
- BeautifulSoup (for news scraping)
- gTTS (Google Text-to-Speech)
- Playsound
- **Noisereduce** (for noise reduction)

## Notes
- Ensure you have the necessary browser drivers (e.g., ChromeDriver) for Selenium.
- Modify the assistant to support additional features if needed.

## License
This project is open-source and available for modification and distribution.

