import time, os, cv2

CHARS = ' .;+*?%S#@'

AM = 6 # Arbitrary Multiplier

def frame_to_ascii(image):
    width = image.shape[0]
    height = image.shape[1]
    new_h = 148
    new_w = int(new_h/height * width)
    image = cv2.resize(image, (AM*new_w, new_h))
    
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    ascii_frame = '\n'.join([''.join([CHARS[pixel//26] for pixel in row]) for row in grayscale])
    return ascii_frame


def video_to_ascii(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("\033[91mCannot open video file. Try again.\033[0m")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            #print("\033[91mCannot receive frame. Exiting...\033[0m")
            break
        
        ascii_frame = frame_to_ascii(frame)
        print(ascii_frame, end="\r") # Will need to add 'clear' instead

if __name__ == "__main__":
    path = input("Paste the path to your video: ")
    path = "media/examples/Meta_PARTNR.webm" if path.strip() == '' else path
    video_to_ascii(path)
