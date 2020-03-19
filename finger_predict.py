import cv2
import os
from keras.models import load_model

def position(result):

    inner_list = result[0]

    maximum  = max(inner_list)
    pos = 0
    for i in inner_list:
        count = 0
        if i == maximum:
            pos = count
        else:
            count +=1


    pred = {
        "ONE": inner_list[0],
        "TWO": inner_list[1],
        "THREE": inner_list[2],
        "FOUR": inner_list[3],
        "FIVE": inner_list[4]
    }

    for key , val in pred.items():

        if val == maximum:
            return key


model = load_model("finger_detector.h5")
#model.summary()

cap = cv2.VideoCapture(0)

while True:

    _ ,frame = cap.read()
    gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    roi = gray_frame[100 : 400 , 200:500]
    main_roi = cv2.resize(roi , (64,64))

    res = model.predict(main_roi.reshape(1,64,64,1))
    print(res)
    #pred = sorted(pred.items(), key = operator.itemgetter(1) , reverse=True)
    print()
    cv2.rectangle(frame, (200 - 1, 100 - 1), (500 - 1, 400 - 1), (255, 255, 255), thickness=1)

    font = cv2.FONT_HERSHEY_COMPLEX
    # cv2.putText(frame,pred[0][0],(100,100),font,1,(0,255,0),2)

    # for txt , one in pred.items() :
    #     if one == 1.0:
    #         cv2.putText(frame,txt,(200,100),font,2,(255,255,255),2)

    txt = position(res)
    cv2.putText(frame , txt , (200,100) , font , 2 , (255,255,255) , 2)
    cv2.imshow("main frame" , frame)
    cv2.imshow("The Box" , roi)


    if cv2.waitKey(30) == ord("q") :
        break

cap.release()
cv2.destroyAllWindows()

