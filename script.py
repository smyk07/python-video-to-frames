# Converting each video frame into a jpg and saving it to ./frames 

# importing moviepy 
from moviepy.editor import VideoFileClip

# importing numpy 
import numpy as np

# importing modules for file manipulation 
import os

# importing PIL for image manipulation 
from PIL import Image

# check for files in the current directory
files = os.listdir("./")
videopath = None

# create ./frames directory 
for file in files: 
    if file == "frames": 
        print("./frames already exists...")
        break
    else: 
        print("Creating ./frames to save frames...")
        os.mkdir("frames") 
        break

# go through each file and check if it is valid
for file in files: 
    if file.endswith(".mp4"): 
        videopath = f"./{file}"
        print(f"Found {videopath}")
        break
    elif len(files) == 0 and file == files[len(files)-1]: 
        print("No Suitable Video File Found...")
        quit()
    else: 
        continue 

# seperating video into individual frames 
clip = VideoFileClip(videopath)

# display fps of clip
print(f"Clip is of {clip.fps} fps.")

# work on individual frames
# set frame_count variable
frame_count = -1
for frame in clip.iter_frames():
    # increase frame count
    frame_count += 1 

    # Create PIL image from np array
    img = Image.fromarray(frame)

    # Save image
    img.save(
        fp=f"./frames/{videopath[:12]}_f{frame_count}.jpg", 
        format="jpeg"
    )
