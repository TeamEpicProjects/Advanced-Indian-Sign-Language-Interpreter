import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import copy
import mediapipe as mp
import PreprocessingFinal as pre

mp_holistic = mp.solutions.holistic  # Holistic model
mp_drawing = mp.solutions.drawing_utils  # Drawing utilities
print("folder name is " + os.getcwd())
Source = os.getcwd() + r"\dataset\new"
Destination = os.getcwd() + r"\dataset\holistics"


def convertVideos(Source, Destination):
    for File in os.listdir(Source):
        Path2 = os.path.join(Source, File)
        Destination2 = os.path.join(Destination, File)
        convertvids(Path2, Destination2)
        print(Path2)
        print(Destination2)


def convertvids(path1, path2):
    cap = cv2.VideoCapture(path1)
    out = cv2.VideoWriter(path2, cv2.VideoWriter_fourcc(
        'm', 'p', '4', 'v'), 20, (700, 500))

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if ret == False:
                break
            myframe, results = pre.mediapipe_detection(frame, holistic)
            # Draw landmarks
            holistics = copy.copy(myframe)

            # black = np.zeros((700, 500, 3), np.uint8)
            myframe = pre.draw_styled_landmarks(myframe, results)
            final = holistics - myframe
            # print(final.shape)
            # print(final.flatten())
            final_rgb = cv2.cvtColor(final, cv2.COLOR_HSV2RGB_FULL)
            # final_gray = cv2.cvtColor(final_rgb, cv2.COLOR_RGB2GRAY)
            ret, final_binary = cv2.threshold(
                final_rgb, 1, 255, cv2.THRESH_BINARY)
            # print(final_binary.shape)
            out.write(final_rgb)
        cap.release()
        out.release()
        cv2.destroyAllWindows()


convertVideos(Source, Destination)
