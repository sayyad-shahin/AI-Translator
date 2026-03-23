# AI Voice Translator Pro

## Overview

AI Voice Translator Pro is a Streamlit-based web application that enables real-time translation of text and voice inputs into multiple languages. The system integrates Speech-to-Text (STT), Machine Translation, and Text-to-Speech (TTS) to provide seamless multilingual communication with audio output.

## Features

* Text-to-text translation across multiple languages
* Voice input support using audio file upload
* Speech-to-text conversion for audio inputs
* Text-to-speech audio generation for translated text
* Downloadable translated audio output
* Support for Hinglish (Romanized Hindi)

## Technology Stack

* Python
* Streamlit
* Speech Recognition / STT module
* Translation model (custom `translate_text` function)
* Text-to-Speech engine (`generate_audio`)
* File handling using Python OS module

## Project Structure

AI-Voice-Translator/
├── app.py
├── translator.py
├── stt.py
├── tts.py
├── assets/
├── outputs/
└── README.md

## System Architecture

The system follows a modular pipeline architecture:

User Input (Text / Voice)
↓
Speech-to-Text Conversion (if voice input)
↓
Text Preprocessing
↓
Translation Engine
↓
Language Selection (Target Language)
↓
Text-to-Speech Conversion
↓
Audio Output Generation

## Installation

### Prerequisites

* Python 3.8 or higher
* pip package manager

### Setup Steps

1. Clone the repository
   git clone [https://github.com/sayyad-shahin/AI-Translator.git](https://github.com/sayyad-shahin/AI-Translator.git)

2. Navigate to project directory
   cd AI-Translator

3. Install dependencies
   pip install -r requirements.txt

4. Run the application
   streamlit run app.py

## Usage

1. Open the web application in browser
2. Select input mode: Text or Voice
3. Enter text or upload audio file
4. Select target language
5. Click Translate and Generate Audio
6. Download or play the output audio

## Supported Languages

* English
* Hindi
* Hinglish
* French
* German
* Spanish
* Arabic
* Chinese

## Modules Description

### Translator Module

Handles language translation using AI-based NLP models.

### Speech-to-Text Module

Converts audio input into text format for processing.

### Text-to-Speech Module

Converts translated text into audio format.

### Streamlit UI Module

Provides interactive web interface for user interaction.

## Limitations

* Accuracy depends on audio quality for voice input
* Hinglish output depends on model capability
* Large audio files may increase processing time

## Future Enhancements

* Real-time microphone input support
* Live conversation translation
* Offline translation model integration
* Improved Hinglish generation model
* Mobile application support

## License

This project is for educational and development purposes. Commercial usage require
