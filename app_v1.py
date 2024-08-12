from flask import Flask, render_template, request, jsonify, send_from_directory
import google.generativeai as genai
from text_to_speech import synthesize_speech
from speech_to_text import transcribe_audio
import os

app = Flask(__name__)

# Configure the Generative AI model
GOOGLE_API_KEY = "AIzaSyCxjpR3SHdPTS9oSxP4_-dKS6zHYBMnwfQ"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index_v1.html')

@app.route('/start_interview', methods=['POST'])
def start_interview():
    initial_prompt = "You are Mr. Sam, a Principal Engineer with 15 years of experience at VB Interviews Private Limited. I am interviewing for a Python Developer position at your company. From now on, our conversation will be an interview scenario, with you asking me questions as if I were a candidate. Please keep the conversation concise."
    response = chat.send_message(initial_prompt)
    
    audio_file = f"ai_speech0.wav"
    synthesize_speech(response.text, os.path.join("static", "audio", audio_file))
    
    return jsonify({
        "question": response.text,
        "audio_file": f"/audio/{audio_file}"
    })

@app.route('/answer', methods=['POST'])
def answer():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided."}), 400

    user_audio_file = request.files['audio']
    user_audio_path = os.path.join("static", "audio", 'recorded_audio.wav')
    user_audio_file.save(user_audio_path)
    
    # Check if the file is a WAV file
    if not user_audio_path.lower().endswith('.wav'):
        return jsonify({"error": "File is not a WAV format."}), 400

    try:
        # Transcribe the audio
        results = transcribe_audio(user_audio_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    user_response = " ".join([item['text'] for item in results])
    response = chat.send_message(user_response)
    audio_file = f"ai_speech{len(chat.history)}.wav"
    synthesize_speech(response.text, os.path.join("static", "audio", audio_file))
    
    return jsonify({
        "question": response.text,
        "audio_file": f"/audio/{audio_file}"
    })

@app.route('/audio/<filename>')
def get_audio(filename):
    return send_from_directory('static/audio', filename)

if __name__ == '__main__':
    if not os.path.exists('static/audio'):
        os.makedirs('static/audio')
    app.run(debug=True)
