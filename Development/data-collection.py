import os
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import numpy as np
import cv2
import keyboard
from datetime import datetime

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")
root.title('Camera')
os.chdir('RAW')
print(datetime.now())
# print(os.path.abspath(os.getcwd()))


def open_popup():
    top = Toplevel(root)
    top.geometry("400x400")
    top.title("Folder")
    ttk.Label(top, text="Select/Create a Folder :",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=15, padx=12, pady=25)

    n = tk.StringVar()
    folder = ttk.Combobox(top, width=25, textvariable=n)
    # Adding combobox drop down list
    folder['values'] = (os.listdir(os.getcwd()))
    folder.grid(column=1, row=15)
    # Shows first folder as a default value
    folder.current(0)

    # folder.current(0)
    def get_folder_name():
        record = False
        if(os.path.isdir(folder.get())):
            os.chdir(folder.get())
            print(os.getcwd())
            top.destroy()
            # root.destroy()
            duration = 2
            cap = cv2.VideoCapture(0)
            codec = cv2.VideoWriter_fourcc(*'XVID')
            qu = 0
            recording_flag = False
            counter = 0
            path = os.path.basename(os.path.normpath(os.getcwd()))
            while True:
                ret, frame = cap.read()
                cv2.imshow('frame', frame)
                #out = cv2.VideoWriter('folder.get()'+'.'+'avi', fourcc, 20.0, (640,  480))
                start_time = datetime.now()
                # converting into seconds
                diff = (datetime.now() - start_time).seconds
                # print(diff)
                ret, frame = cap.read()
                key = cv2.waitKey(1)
                if key & 0xFF == ord("q"):
                    break
                elif key & 0xFF == ord("s"):
                    if recording_flag == False:
                        while os.path.exists("%s%s.avi" % (path, counter)):
                            counter += 1
                        while(diff <= duration):
                            ret, frame = cap.read()
                            cv2.putText(frame, str(diff), (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (255, 0, 0), 2, cv2.LINE_AA)  # adding timer text
                            cv2.imshow('frame', frame)
                            # out.write(frame)
                            # count=counter+1
                            diff = (datetime.now() - start_time).seconds
                            output = cv2.VideoWriter("%s%s.avi" % (
                                path, counter), codec, 20.0, (640, 480))
                            recording_flag = True
                            k = cv2.waitKey(10)
                            if k & 0xFF == ord("r"):  # reset the timer
                                break
                        # counter+=1
                    else:
                        recording_flag = False

                if recording_flag:
                    output.write(frame)

            cap.release()
            output.release()
            cv2.destroyAllWindows()
        else:
            os.chdir('../roots')
            lowfold = folder.get().lower()
            os.mkdir(lowfold)
            os.chdir(lowfold)
            print(os.getcwd())
            top.destroy()
            # os.chdir('roots')
            # root.destroy()
            duration = 2
            cap = cv2.VideoCapture(0)
            codec = cv2.VideoWriter_fourcc(*'XVID')
            qu = 0
            recording_flag = False
            counter = 0
            path = os.path.basename(os.path.normpath(os.getcwd()))
            while True:
                ret, frame = cap.read()
                cv2.imshow('frame', frame)
                #out = cv2.VideoWriter('folder.get()'+'.'+'avi', fourcc, 20.0, (640,  480))
                start_time = datetime.now()
                # converting into seconds
                diff = (datetime.now() - start_time).seconds
                # print(diff)
                ret, frame = cap.read()
                key = cv2.waitKey(1)
                if key & 0xFF == ord("q"):
                    print('Closed')
                    break
                elif key & 0xFF == ord("s"):
                    if recording_flag == False:
                        while os.path.exists("%s%s.avi" % (path, counter)):
                            counter += 1
                        while(diff <= duration):
                            ret, frame = cap.read()
                            cv2.putText(frame, str(diff), (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (255, 0, 0), 2, cv2.LINE_AA)  # adding timer text
                            cv2.imshow('frame', frame)
                            # out.write(frame)
                            # count=counter+1
                            diff = (datetime.now() - start_time).seconds

                            k = cv2.waitKey(10)
                            if k & 0xFF == ord("r"):  # reset the timer
                                break
                        output = cv2.VideoWriter("%s%s.avi" % (
                            path, counter), codec, 20.0, (640, 480))
                        recording_flag = True
                    else:
                        recording_flag = False

                if recording_flag:
                    output.write(frame)

            cap.release()
            output.release()
            cv2.destroyAllWindows()

    button = Button(top, text="Create", command=get_folder_name)
    button.grid(row=18, column=1)
    top.resizable(0, 0)
    top.lift()
    top.grab_set()


button = Button(root, text="Start", command=open_popup)
button.grid(row=8, column=1)
root.mainloop()
