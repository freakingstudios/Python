import pygame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from threading import Thread

# Function to update the visualization
def update_visualization(frame):
    # Clear the previous plot
    plt.clf()

    # Get the current frequency data
    freq_data = np.fft.fft(stream.get_samples())[1:fft_size//2]
    frequencies = np.fft.fftfreq(fft_size, 1/sample_rate)[:fft_size//2]

    # Plot the frequency data
    plt.plot(frequencies, np.abs(freq_data))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Music Visualizer')

    # Adjust the plot limits
    plt.ylim(0, 20000)
    plt.xlim(0, sample_rate/2)

    # Show the plot
    plt.pause(0.001)

# Function to play audio
def play_audio():
    stream.play()

# Initialize pygame
pygame.init()

# Initialize the audio stream
sample_rate = 44100
buffer_size = 1024
fft_size = 2048

pygame.mixer.init(sample_rate, -16, 1, buffer_size)
stream = pygame.mixer.Sound('your_audio_file.wav')

# Create the visualization window
fig = plt.figure(figsize=(8, 4))
plt.subplots_adjust(bottom=0.15)
plt.grid()

# Start the audio playback in a separate thread
audio_thread = Thread(target=play_audio)
audio_thread.start()

# Start the animation
ani = animation.FuncAnimation(fig, update_visualization, interval=10)
plt.show()

# Wait for the audio playback to finish
audio_thread.join()
