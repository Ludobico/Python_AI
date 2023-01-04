import cv2
import os
import torch
import numpy

print(torch.cuda.is_available())

objectTracking = torch.hub.load('WongKinYiu/yolov7','custom', path='./volov7_objectTracking/weights/best.pt',force_reload=True)
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Unable to read camera")

else:

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))


    out = cv2.VideoWriter('data/videos/output.avi',
                        cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                        10,
                        (frame_width, frame_height) )
                        
    while True:
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            frame = objectTracking(frame)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break
            
    cap.release()
    out.release()
    cv2.destroyAllWindows()
