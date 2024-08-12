from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from text_to_speech import synthesize_speech, play_audio
from speech_to_text import record_audio, transcribe_audio

app = Flask(__name__)

# Configure the Generative AI model
GOOGLE_API_KEY= "AIzaSyCxjpR3SHdPTS9oSxP4_-dKS6zHYBMnwfQ"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index_v0.html')

@app.route('/start_interview', methods=['POST'])
def start_interview():
    initial_prompt = "You are Mr. Sam, a Principal Engineer with 15 years of experience at VB Interviews Private Limited. I am interviewing for a Python Developer position at your company. From now on, our conversation will be an interview scenario, with you asking me questions as if I were a candidate. Please keep the conversation concise."
    response = chat.send_message(initial_prompt)
    
    synthesize_speech(response.text, "ai_speech0.wav")
    
    return jsonify({
        "question": response.text,
        "audio_file": "ai_speech0.wav"
    })

@app.route('/answer', methods=['POST'])
def answer():
    user_response = request.json.get('answer')
    response = chat.send_message(user_response)

    # Create AI's speech
    audio_file = f"ai_speech{len(chat.history)}.wav"
    synthesize_speech(response.text, audio_file)
    
    return jsonify({
        "question": response.text,
        "audio_file": audio_file
    })

if __name__ == '__main__':
    app.run(debug=True)
