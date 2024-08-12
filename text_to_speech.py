import pyttsx3
import pygame

def synthesize_speech(text, output_file_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file_path)
    engine.runAndWait()

def play_audio(output_file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(output_file_path)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage
# text = "Hello, Mrs Bhavani, Doobbi Tinnavaa? Wife of P K V Nath. Mother of P S S K Nath and P Moulika"
# output_file_path = 'output_speech.wav'
# while True:
#     synthesize_speech(text, output_file_path)
