import cv2

def extract_frames(video_path):
    frames = []
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Cannot open video {video_path}")
        return frames

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    
    cap.release()
    return frames

import cv2

def save_frames_as_video(frames, output_path, fps):
    if not frames:
        print("No frames to save.")
        return
    
    # Get frame height, width, and channel information from the first frame
    height, width, layers = frames[0].shape
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID' or other codecs
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame in frames:
        out.write(frame)
    
    out.release()
    print(f"Video saved to {output_path}")

# Example usage:
# Assuming you have a list of frames from the previous example
# frames = extract_frames('c:/Users/vibha/OneDrive/Desktop/BADMINTON/videos/input_video.mp4')

# output_video_path = 'c:/Users/vibha/OneDrive/Desktop/BADMINTON/videos/output_video.mp4'
# fps = 30  # Set your desired frames per second

# save_frames_as_video(frames, output_video_path, fps)
