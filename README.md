# Advanced-Indian-Sign-Language-Interpreter

## Problem Statement
Create an automated engine able to recognize some ISL gestures. As per statistics, there are 1.8 million people with hearing and speech imparity, and only 250 certified sign language interpreters exist throughout the nation which comes to a ratio of 1:7200. This count of human interpreters is inefficient and inadequate. Sign language is the basic communication method used by hearing and speech-disabled people. People with hearing and speech disabilities face problems in communicating with other normal people without a translator. For this reason, the implementation of a system that recognizes sign language will have a significant impact on the life of the disabled. Common tools are just able to use still images as input; in this project, we want to overcome that limitation by working on small videos. Also, the engine for the classification is typically slow and not very performing, and would be great to move it to a Deep-Learning model. 

## Technology stack

Software Requirements: Pycharm/Jupyter notebooks, Anaconda 

Libraries: Keras, OpenCV, TensorFlow, NumPy, SciPy, pandas 

## Instructions:
Video Preprocessing:
In order to check the image preprocessing part run the script PreprocessingFinal using the command python PreprocessingFinal.py  

Data Manipulation:  
In order to resize the captured videos run the video-resize script using the command python video-resize.py  
After resizing is done you can apply the preprocessing on that to generate the final result by running the convert-videos script using command python convert-videos.py  

Video Prediction:  
the prediction can be tested by running the script mainmodel using command python mainmodel.py  

## Architecture diagram
![image](https://user-images.githubusercontent.com/43364258/141424707-b67cc198-4609-4731-839c-91aa4a4d4d31.png)
