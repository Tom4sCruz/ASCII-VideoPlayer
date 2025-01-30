import cv2
import numpy as np
import os
import time

# ASCII characters from dark to light
ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(frame, width=100):
    """Convert a frame to an ASCII string."""
    # Resize frame
    height = int(frame.shape[0] * (width / frame.shape[1] * 0.55))  # Adjust aspect ratio
    frame = cv2.resize(frame, (width, height))

    # Convert to grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Normalize pixel values and map to ASCII
    ascii_frame = "\n".join(
        "".join(ASCII_CHARS[pixel // (256 // len(ASCII_CHARS))] for pixel in row)
        for row in grayscale
    )
    return ascii_frame

def play_video_ascii(video_path, width=100, fps_limit=30):
    """Play a video in ASCII format in the terminal."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1 / min(fps, fps_limit)  # Control frame rate

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Stop when the video ends

        ascii_frame = frame_to_ascii(frame, width)
        os.system("clear" if os.name == "posix" else "cls")  # Clear terminal
        print(ascii_frame)

        time.sleep(frame_delay)  # Control playback speed

    cap.release()

if __name__ == "__main__":
    video_path = "yt_sunset.mp4"
    play_video_ascii(video_path)

