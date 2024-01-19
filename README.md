# Gita-QR-Code-Detection

### About this repository:
This code was used for an undergraduate research class. The final goal was to asses how older adults would respond to using a person-follower cargo carrying robot. Questions would be asked after these older adults used the robot. Conculsions would be made to see how these types of robots could be used for assitive technology applications.  
After performing a literature review, we discoverd there is a lack of testing
procedures to properly asses saftey between autonomous robots interacting with people. Therfore, a subgoal of this research was to 
contribute to the testing protocol of a person-follower cargo carrier robot. The QR distance detection code will obtain the following and braking distance of the robot. 
Various tests were conducted with two walking speeds, varying the weight in the robot, and varying the ground surface. Videos recoreded from a paticular trial can be placed
into a folder. Analysis will then be run on videos in the folder; annotations (bounding boxes) will be drawn on the video, and the distances will be saved to a csv files to 
be later plotted. An example is shown below.

[![Watch the video](https://img.youtube.com/vi/<VIDEO_ID>/hqdefault.jpg)]([https://www.youtube.com/embed/<VIDEO_ID>](https://youtu.be/m0nJvtGD3NA))

[<img src="https://img.youtube.com/vi/m0nJvtGD3NA/hqdefault.jpg" width="400" height="300"
/>](https://www.youtube.com/embed/m0nJvtGD3NA)

### General Steps to Run Any of the Code: 
1.) Clone the repo in the directory of your choosing. 

2.) Ensure that you have python and pip installed using:  
python --version OR python3 --version  
pip --version 

If command is not recognized, proceed to install them. 

3.) **Optional**: Setup a python virtual environment. This is only
applicable if you frequently use python and want to manage interdependency problems  

4.) Run the following command in the terminal:  
pip install opencv-python  
pip install matplotlib  

### Steps to Run QR_LiveWebcam.py  

1.) Familiarize yourself with the Qr-Detector, open **QR_LiveWebcam.py** file  
in your favorite code editor. The code should be ready to run at this point. 

2.) Run QR_LiveWebcam.py using:  
python distance2.py OR python3 distance2.py 
OR hit the run button in your IDE. 

3.) Your webcam should launch. If a QR code is placed in view, a bounding box should
be drawn tightly around it. The distance to the camera shoudld also be displayed in text.

4.) Since the resolution of my webcam and your webcam are likely different, the distance 
calculation will likely be innacurate, but the code should not crash. 

5.) Close the program by pressing 'q' on the keyboard.  

6.) Notice new directories are created: 
"csvFiles" and "videoOutput"  
The csv files store the distance measurments. The videos are the recorded with the opencv  
markings on top of the video (bounding box and text). 
Both files are saved as names with the date and hour of recording/processing. 

### Setup Procudure for find_Ref_img.py (prior to running QR_RecordedVid.py)

1.) Tape QR-code paper to desired location.  

2.) Measure horizontal distance between QR-code and camera. The camera and QR-code 
should be on the same horizontal plane.

3.) On line 10 of QR_RecordedVid.py, update the constant "KNOWN_DISTANCE" with this  
measured distance. (units must be in centimeters)  

4.) Record a video of the QR-code at the same height and same distance away from  
step 2.). There should be no movement in this video. The purpose of this video is  
to find a suitable refrence image and have accurate distance readings. 

5.) Place this video in the same directory as find_Ref_Img.py  

6.) Input new video name in line 5 of find_Ref_Img.py: 
cap = cv2.VideoCapture("IMG_3214.MOV")  

7.) Run find_Ref_Img.py  
This will generate a suitable image named "referenceImg.jpg". It will be used for
QR_RecordedVid.py 

### Steps to run QR_RecordedVid.py)

**Note: Setup Procudure for find_Ref_img.py only needs to be done once (If recording is  
always done at same height and same procedure).**

1.) Record video where camera and QR-code are on the same plane. Video should involve
walking with the robot. Video should be as high quality as possible (4k)

2.) Place video in same directory as QR_RecordedVid.py

3.) Edit line 14 of QR_RecordedVid.py:  
cap = cv2.VideoCapture("IMG_3214.MOV")  
replace with new video name. 

4.) Run the script. Notice the progress print statments in the terminal.

5.) The distance plot will be displayed at the end of processing.  

6.) To finish the script, the plot must be closed. The script cannot be rerun  
unless the plot is first closed.  


