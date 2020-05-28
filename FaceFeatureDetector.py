import cv2

import os

face_classifier=cv2.CascadeClassifier("C:/Users/LRG/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

eye_classifier=cv2.CascadeClassifier("C:/Users/LRG/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_eye.xml")

path="E:/doop"#any folder to strore the captured images

cap=cv2.VideoCapture(1) # it depends upon the port assigned 0 or 1 are mostly available

counts=0

while(1):

    counts+=1

    _, img = cap.read()

    faces = face_classifier.detectMultiScale(img,1.4,5)  # 3-6 is good value for min neighbours

    eyes = eye_classifier.detectMultiScale(img)

    x,y,w,h=0,0,0,0

    for x,y,w,h in faces:

        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2,cv2.LINE_AA)

        for q,w,r,s in eyes:

            img = cv2.rectangle(img, (q, w), (q + r, w + s), (0, 255, 255), 2, cv2.LINE_AA)

            
    #you can save the photos using following line..each frame is saved with a unique number
            
    #cv2.imwrite(os.path.join(path, "img_" + str(counts) + ".jpg"), img[y:y + h, x:x + w])
    print(img)

    cv2.imshow("oo",img)

    ch=cv2.waitKey(1)

    if ch==27 or counts==250: #at max 150 frames are captured

        break

cap.release()

cv2.destroyAllWindows()
