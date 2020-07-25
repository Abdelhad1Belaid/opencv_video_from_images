import cv2
import os
from os.path import isfile, join
path = '' #images path ends with '/' 
frames = []
time = 20
fps = 1

files = [f for f in os.listdir(path) if isfile(join(path, f))]
for i in range(len(files)):
    filename = path + files[i]
    img = cv2.imread(filename)
    
    # img = cv2.resize(img,(width,height))
    '''to resize images in case they are not in same size '''

    height, width, layers = img.shape
    size = (width, height)

    for k in range(time):
        frames.append(img)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path, fourcc, fps, size)

    for j in range(len(frames)):
        out.write(frames[i])
    out.release()
