import cv2
import os

print("file name is " + os.getcwd())
Source = os.getcwd() + r"\dataset\old"
Destination = os.getcwd() + r"\dataset\new"


def resizedVideos(Source, Destination):
    for File in os.listdir(Source):
        Path2 = os.path.join(Source, File)
        Destination2 = os.path.join(Destination, File)
        Resized(Path2, Destination2)
        # print(File)
        # for Video in os.listdir(Path2):
        # Path3 = os.path.join(Path2, Video)
        # Destination3 = os.path.join(Destination2, Video)
        # Resized(Path3, Destination3)


def Resized(path1, path2):
    cap = cv2.VideoCapture(path1)
    out = cv2.VideoWriter(path2, cv2.VideoWriter_fourcc(
        'm', 'p', '4', 'v'), 20, (320, 320))
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv2.resize(frame, (320, 320))
        # print(frame)
        # print(path2)
        # Display the resulting frame
        out.write(frame)
        # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()


resizedVideos(Source, Destination)
