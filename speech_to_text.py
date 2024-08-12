import pyaudio
import wave
from vosk import Model, KaldiRecognizer
import json

def record_audio(output_file_path, duration=10, sample_rate=16000, chunk_size=1024):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)
    print("Recording...")
    frames = []
    for _ in range(int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)
    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(output_file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

def transcribe_audio(audio_file_path):
    model_path = r"C:\Users\saipa\Downloads\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15"
    model = Model(model_path)
    wf = wave.open(audio_file_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    
    return results

# Record and transcribe
# audio_file_path = 'recorded_audio.wav'
# record_audio(audio_file_path)
# results = transcribe_audio(audio_file_path)
# answer = " ".join([item['text'] for item in results])
# print(answer)