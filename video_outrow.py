import cv2
import os 

def animation_outrow():
    cap=cv2.VideoCapture("bye-bye.mp4")
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            cv2.imshow("Outrow", frame)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        else:
            cap.release()
            cv2.destroyAllWindows()
            #os.system("shutdown /s /t 1")
    else:
        print("Error")
if __name__ == "__main__":
    animation_outrow()
