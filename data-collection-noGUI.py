import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import pickle
import time

# Tried but obsolete so has been commented out


def nothing(x):
    pass


def read_image():
    cap = cv2.VideoCapture(0)
    keyc, keys = False, False
    while True:
        key = cv2.waitKey(1)
        _, frame = cap.read()
        flip = cv2.flip(frame, 1)

        cv2.imshow("RAW", flip)

        '''
		Here we check for input key
		'''

        if key == ord('s'):
            "write code to start saving short clips"
            cap.release()
            cv2.destroyAllWindows()
            ########
            save_images(path())

        if key == ord('x'):
            cap.release()
            cv2.destroyAllWindows()
            break
        '''
		depending on key pressed we take the action we want to
		'''
        if keyc:
            cv2.imshow("back project", back)


def path():
    path = os.getcwd()
    path = os.path.join(path, 'RAW')
    word = input("Enter the letter you want to save:\n").lower()
    if os.path.exists(path):
        path = os.path.join(path, word)
        if not(os.path.exists(path)):
            os.mkdir(path)
    else:
        os.mkdir(path)
        path = os.path.join(path, word)
        os.mkdir(path)
    return path


def save_images(path_og, roi_hist):
    cap = cv2.VideoCapture(0)
    keyc = False
    keyx = False
    new_file = []
    frame_count = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        _, frame = cap.read()
        key = cv2.waitKey(1)
        flip = cv2.flip(frame, 1)
        cv2.imshow("flip", flip)
        if key == ord('r'):
            cap.release()
            cv2.destroyAllWindows()
            path_og = path()
            save_images(path_og)
        if key == ord('c'):
            keyc = True
        if keyc:
            frame_count = frame_count + 1
            if frame_count > 70:

                files = os.listdir(path_og)
                ext = ".png"
                if files == []:
                    name = 0
                else:
                    for file in files:
                        file = file.split('.')
                        new_file.append(int(file[0]))
                    new_file.sort()
                    name = new_file[-1]
                for n in range(300):
                    _, frame = cap.read()
                    flip = cv2.flip(frame, 1)

                    name = name + 1
                    imgname = str(name) + '.png'
                    imgname = os.path.join(path_og, imgname)
                    flip = cv2.resize(flip, (50, 50))
                    cv2.imwrite(imgname, flip)

                    normal = cv2.flip(flip, 1)
                    name = name + 1
                    imgname = str(name) + '.png'
                    imgname = os.path.join(path_og, imgname)
                    cv2.imwrite(imgname, normal)
                    print(imgname)
                keyc = False
        if key == ord('x'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    read_image()
