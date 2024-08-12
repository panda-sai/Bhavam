# BHAVAM - AI Interview Preparation App

## Overview

The AI Interview Preparation App is an advanced tool designed to help users simulate real-life interview scenarios and receive personalized feedback. Powered by AI and leveraging Google's Gemini API, the app allows users to practice answering interview questions tailored to their desired job role and experience level. The app not only conducts the interview but also provides insightful feedback, helping users improve their performance and build confidence for their actual interviews.

[![DEMO VIDEO](https://img.youtube.com/vi/45nmovxQYHI/0.jpg)](https://youtu.be/45nmovxQYHI)


## Features

- **AI-Powered Interviews:** Simulate real-world interview scenarios with an AI interviewer that asks dynamic, context-aware questions.
- **Personalized Feedback:** Receive detailed feedback on your answers, highlighting strengths and areas for improvement.
- **Voice Interaction:** Record your answers in real-time and interact with the AI through voice commands.
- **Comprehensive Preparation:** Tailored interview questions based on your experience level and the specific job role you're applying for.
- **Anywhere, Anytime:** Practice interviews on your schedule with an AI coach that's available 24/7.

## Versions

The project includes three versions, each progressively enhancing the user experience:

### Version 0 - Text to Text Conversation
In this version, the interaction between the user and the AI interviewer is text-based. 

To run this version:
```bash
python app_v0.py
```
### Version 1 - Voice to Voice Conversation
This version upgrades the experience to a voice-based interaction, where users can speak their answers, and the AI interviewer responds with audio.

To run this version:
```bash
python app_v1.py
```

Note: If you encounter the "RRID error" due to browser audio format inconsistencies, you can test the voice interaction on the command line by running:

```bash
python ai_interview.py
```

### Version 2 - Video to Video (In Progress)
The upcoming version will include video-based interactions, creating a more immersive interview experience.

To test the video functionality:

1. Uncomment the "Generate Video" and "Play Video" parts of the code in ai_interview.py.
2. Ensure that you have set up SadTalker in the same repository location as the current project. Instructions to setup can be found here: [YouTube Link](https://youtu.be/yEkLEm-10Mw?feature=shared)

## Usage
### Prerequisites
1. Python 3.8+
2. Flask
3. Google's Gemini API Key

## Installation
Clone this repository:

```bash
git clone https://github.com/panda-sai/Bhavam.git
cd Bhavam
```
Install the required Python packages:
```bash
pip install -r requirements.txt
```
Set up your environment with your Google Gemini API key:
```bash
export GOOGLE_API_KEY="your_google_api_key"
```

###### Run the Flask app according to the version you wish to test (e.g., app_v0.py, app_v1.py, or ai_interview.py).

### Using the App
Open your web browser and navigate to http://127.0.0.1:5000.
Start the interview according to the selected version.
Follow the prompts, recording or typing your answers.
Review the AI-generated feedback and improve your responses.

## Gemini API Integration
The AI Interview Preparation App uses Google's Gemini API to deliver a seamless and realistic interview experience. The API powers the AI interviewer, enabling it to ask context-aware questions and provide detailed feedback based on your responses. This feedback includes an analysis of the content, tone, and structure of your answers, helping you refine your interview skills.

## Contributing
We welcome contributions to improve this app! If you have suggestions or find issues, please submit a pull request or open an issue.