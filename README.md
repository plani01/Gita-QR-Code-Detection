# Gita-QR-Code-Detection

### Steps to Run Code: 
1.) Clone the repo in the directory of your choosing. 

2.) Ensure that you have python and pip installed using:  
python --version OR python3 --version  
pip --version 

If command is not recognized, proceed to install them. 

3.) **Optional**: Setup a python virtual environment. This is only
applicable if you frequently use python and want to manage interdependency problems  

4.) Run the following command in the terminal:  
pip install opencv-python  

5.) Familiarize yourself with the Qr-Detector using your webcam by opening the **distance2.py** file  
in your favorite code editor. The code should be ready to run at this point. 

6.) Run distance2.py using:  
python distance2.py OR python3 distance2.py 
OR hit the run button in your IDE. 

7.) Your webcam should launch. If a QR code is placed in view, a bounding box should
be drawn tightly around it. The distance to the camera shoudl also be displayed in text.

8.) Since the resolution of my webcam and your webcam are likely different, the distance 
calculation will likely be innacurate, but the code should not crash. 

9.) Close the program by pressing 'q' on the keyboard.  

10.) Notice new directories are created: 
"csvFiles" and "videoOutput"  
The csv files store the distance measurments. The videos are the recorded with the opencv  
markings on top of the video (bounding box and text). 
Both files are saved as names with the date and hour of recording/processing. 

10.) Perform Qr-Code validation testing using the Gita **Using distance3.py** : 
- First run distance3.py first by itself: Notice how a large distorted video starts playing
  - This is a 4k video I recorded using my phone, wait for the program to finish(1-2 min maximum)
  - final video with bounding box processing on top will be found in the videoOutput folder
  - Later, you will replace the input video provided with your own video
- Tape a picture of large QR code to the front face of the Gita.  
- Record High quality (4k, HD ) videos on your smartphone
- Upload video to your computer and place it in the same directory as the repo
- Replace line 28 with the new video name
- The distance calculation is expected to be buggy and innacurate, this is not the main focus. 

