import cv2
import os

# Object to read video file
cap = cv2.VideoCapture("GH013693.mp4")

# Object to do QR Code detection
qrDecoder = cv2.QRCodeDetector()

"""Getting info about video resolution"""
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

print("frame width: ", frame_width, "\n")
print("frame height: ", frame_height, "\n")

fileNumber = 0

while(cap.isOpened):
    ret, frame = cap.read()

    if not ret: # ret is false means last frame 
        break

    # perform QR-code detection on current video frame
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)

    # check if QR code detected 
    if len(data)>0:
        print("Reference image from video frame# ", str(fileNumber))
        cv2.imwrite("referenceImg.jpg", frame)
        break
        #print("Decoded Data : {}".format(data))
        #display(inputImage, bbox)
        #rectifiedImage = np.uint8(rectifiedImage)
        #cv2.imshow("Rectified QRCode", rectifiedImage)
    else:
        print("QR Code not detected from frame# " ,str(fileNumber))
        #cv2.imshow("Results", inputImage)

    fileNumber +=1

    
    # End processing early by pressing 'q'
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

print("Program has Finished")

