import cv2
import numpy as np
import os
from datetime import datetime

# variables
# distance from camera to object(face) measured from refrence image
KNOWN_DISTANCE = 165.1  # centimeter (23 inches)
# width of face in the real world or Object Plane
KNOWN_WIDTH = 13.9  # centimeter, keepting old

# array of stored distances 
distanceArray = []

# get current time: used to save unique files
now = datetime.now()
timeStr = now.strftime("%m-%d-%Y, %H.%M.%S")


# Colors
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
fonts = cv2.FONT_HERSHEY_COMPLEX

#object used to get video frames, either live from webcam or from 
# video file 
cap = cv2.VideoCapture("IMG_3214.MOV")

#used to write video 
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

print("frame width: ", frame_width, "\n")
print("frame height: ", frame_height, "\n")

#face_detector = cv2.CascadeClassifier("C:/Users/plani/OneDrive/Desktop/Gita Testing Code/Gita-Testing/Distance_measurement_using_single_camera/haarcascade_frontalface_default.xml")
qrDecoder = cv2.QRCodeDetector()

# focal length finder function
def focal_length(measured_distance, real_width, width_in_rf_image):
    """
    This Function Calculate the Focal Length(distance between lens to CMOS sensor), it is simple constant we can find by using
    MEASURED_DISTACE, REAL_WIDTH(Actual width of object) and WIDTH_OF_OBJECT_IN_IMAGE
    :param1 Measure_Distance(int): It is distance measured from object to the Camera while Capturing Reference image

    :param2 Real_Width(int): It is Actual width of object, in real world (like My face width is = 14.3 centimeters)
    :param3 Width_In_Image(int): It is object width in the frame /image in our case in the reference image(found by Face detector)
    :retrun focal_length(Float):"""
    focal_length_value = (width_in_rf_image * measured_distance) / real_width
    return focal_length_value


# distance estimation function
def distance_finder(focal_length, real_face_width, face_width_in_frame):
    """
    This Function simply Estimates the distance between object and camera using arguments(focal_length, Actual_object_width, Object_width_in_the_image)
    :param1 focal_length(float): return by the focal_length_Finder function

    :param2 Real_Width(int): It is Actual width of object, in real world (like My face width is = 5.7 Inches)
    :param3 object_Width_Frame(int): width of object in the image(frame in our case, using Video feed)
    :return Distance(float) : distance Estimated
    """
    distance = (real_face_width * focal_length) / face_width_in_frame
    return distance

# face detector function
def qr_detect(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    __,bbox,__ = qrDecoder.detectAndDecode(gray_image)

    #print("variable type of bbox: ", type(bbox))
    #print(bbox)

    if bbox is not None:
        bbox3 = np.empty( shape=(1,4,2), dtype=np.dtype('int'))
        

        for j in range(4):
            bbox3[0][j][0] = int(bbox[0][j][0])
            bbox3[0][j][1] = int(bbox[0][j][1])

        #print("cord1:", bbox3[0][0], "cord2:", bbox3[0][1] )
        #print("width is: ", bbox3[0][1][0], " - ", bbox3[0][0][0] )
        #print("width:", width)

        width = bbox3[0][1][0] - bbox3[0][0][0]

        cv2.line(image, bbox3[0][0], bbox3[0][1], (255,0,0), 3)
        cv2.line(image, bbox3[0][2], bbox3[0][1], (255,0,0), 3)
        cv2.line(image, bbox3[0][2], bbox3[0][3], (255,0,0), 3)
        cv2.line(image, bbox3[0][0], bbox3[0][3], (255,0,0), 3)
        return width
    return 0

# reading reference image from directory
ref_image = cv2.imread("CBOL8916.JPG")
#ref_image = cv2.resize(ref_image, fx=0.1,fy=0.1, dsize= (1280,720), interpolation=cv2.INTER_AREA ) #interpolation=cv2.INTER_AREA

print("refrence image dimensions", ref_image.shape)

ref_image_face_width = qr_detect(ref_image)

print("ref image width: ", ref_image_face_width)

focal_length_found = focal_length(KNOWN_DISTANCE, KNOWN_WIDTH, ref_image_face_width)
print("focal length found is: ", focal_length_found)
cv2.imshow("ref_image", ref_image)

video_Dir_name = "videoOutput"
IsDirExist = os.path.exists(video_Dir_name)
if not IsDirExist:
        os.mkdir(video_Dir_name)

csv_Dir_name = "csvFiles"
IsDirExist = os.path.exists(csv_Dir_name)
if not IsDirExist:
        os.mkdir(csv_Dir_name)

out = cv2.VideoWriter( "videoOutput/" + timeStr + ".avi",cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))

while(cap.isOpened):
    ret, frame = cap.read()

    if not ret: # ret is false means last frame 
        break
    qr_width_in_frame = qr_detect(frame)

    # finding the distance by calling function Distance
    if qr_width_in_frame != 0 and qr_width_in_frame > 0:

        Distance = distance_finder(focal_length_found, KNOWN_WIDTH, qr_width_in_frame)
        
        distanceArray.append(round(Distance,3))
        # Drwaing Text on the screen
        cv2.putText(
            frame, f"Distance = {round(Distance,2)} CM", (50, 50), fonts, 1, (RED), 2
        )
    else:
        distanceArray.append(0)

    # calling face_data function
    cv2.imshow("frame", frame)

    out.write(frame)

    if cv2.waitKey(1) == ord("q"):
        break
np.savetxt("csvFiles/"+timeStr + ".csv", distanceArray, delimiter=', ', fmt='%1.3f')
cap.release()
cv2.destroyAllWindows()

print("0: success")