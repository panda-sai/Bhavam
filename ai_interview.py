import google.generativeai as genai
from text_to_speech import synthesize_speech, play_audio
from speech_to_text import record_audio, transcribe_audio
from video_gen import generate_video, play_video

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
     
response = chat.send_message("You are Mr. Sam, a Principal Engineer with 15 years of experience at VB Interviews Private Limited. I am interviewing for a Python Developer position at your company. From now on, our conversation will be an interview scenario, with you asking me questions as if I were a candidate. Please keep the conversation concise.")
print(response.text)
i=0
while True:
    synthesize_speech(response.text, "ai_speech"+str(i)+".wav")
    play_audio("ai_speech"+str(i)+".wav")

    # # Generate Video
    # generate_video(ai_speech_path,image_path)
    # # Play Video
    # play_video(r"SadTalker\results\2024_08_11_18.26.08\temp_image##ai_speech0.mp4") 

    record_audio("human_speech"+str(i)+".wav")
    results = transcribe_audio("human_speech"+str(i)+".wav")
    answer = " ".join([item['text'] for item in results])
    print(answer)

    response = chat.send_message(answer)
    print(response.text)
    i = i+1

