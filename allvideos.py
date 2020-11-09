#https://stackoverflow.com/questions/54962504/how-do-i-extract-the-frames-from-a-folder-of-mp4-videos-and-transfer-them-to-ano

import cv2
import math
import glob

def video2frames(video_file_path):
    count = 0
    cap = cv2.VideoCapture(video_file_path)
    frame_rate = cap.get(5)
    while cap.isOpened():
        frame_id = cap.get(1)
        ret, frame = cap.read()
        if not ret:
            break
        if frame_id % math.floor(frame_rate) == 0:
            filename = '{}_frame_{}.jpg'.format(video_file_path, count)
            count += 1
            cv2.imwrite(filename, frame)
    cap.release()

videos = glob.glob('C:\\Users\\sanja\\OneDrive\\Desktop\\Regis\\Data Science PracticimII(MSDS 696)\\Bodyscans\\*.mkv') #Video Folder
for i, video in enumerate(videos):
    print('{}/{} - {}'.format(i+1, len(videos), video))#wriring images in the format
    video2frames(video)