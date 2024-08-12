import subprocess
import pygame
from moviepy.editor import VideoFileClip

# Construct the command as a list of arguments
def generate_video(driven_audio, source_image):
    command = [
    'cd SadTalker py -3.8', 'inference.py',
    '--driven_audio', driven_audio,
    '--source_image', source_image,
    '--result_dir', './results',
    '--still',
    '--preprocess', 'full',
    '--enhancer', 'gfpgan'
    ]

    try:
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
    
        # Print the output and error messages
        print("Output:", result.stdout)
        print("Error:", result.stderr)
        return result
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def play_video(video_path):
    # Initialize Pygame
    pygame.init()
    
    # Load the video file
    clip = VideoFileClip(video_path)
    
    # Set up the display
    screen = pygame.display.set_mode((clip.w, clip.h))
    clock = pygame.time.Clock()
    
    # Play the video
    for frame in clip.iter_frames(fps=24):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Convert frame to Pygame surface
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        
        # Display the frame
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        
        # Limit frame rate
        clock.tick(24)
    
    pygame.quit()

# Example usage
# play_video(r"C:\Temp Project\SadTalker\results\2024_08_11_18.26.08\temp_image##ai_speech0.mp4")
