import os
import cv2 as cv

dir = r"D:/video/video/"

l = [dir + os.listdir(dir)[i] for i in range(len(os.listdir(dir)))]

def with_opencv(l):
    d = []
    for i in l:
        cap = cv.VideoCapture(i)
        fps = cap.get(cv.CAP_PROP_FPS)
        frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
        duration = frame_count/fps
        minutes = str(int(duration/60))
        seconds = str(int(duration%60))
        d.append(i + ", длительность: " + minutes + ":".rstrip() + seconds.lstrip())
    
    print(d)
    return minutes, seconds
