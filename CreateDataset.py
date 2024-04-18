import os

import mediapipe as mp
import cv2
import pickle
import matplotlib.pyplot as plt

mpHands = mp.solutions.hands
mpDrawing = mp.solutions.drawing_utils
mpDrawingStyles = mp.solutions.drawing_styles

hands = mpHands.Hands (static_image_mode = True, min_detection_confidence = 0.3)

dataDir = './data'

data = []
labels = []

for cPath in os.listdir(dataDir):
    print (cPath)
    for imgPath in os.listdir(os.path.join(dataDir, cPath)):
        data_aux = []
        img = cv2.imread(os.path.join(dataDir, cPath, imgPath))
        rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(rgbImg)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)
                    
                    #print(hand_landmarks.landmark[i])
                #mpDrawing.draw_landmarks (
                #    rgbImg,
                #    hand_landmarks,
                #    mpHands.HAND_CONNECTIONS,
                #    mpDrawingStyles.get_default_hand_landmarks_style(),
                #    mpDrawingStyles.get_default_hand_connections_style())
            data.append(data_aux)
            labels.append(cPath)
#        plt.figure()
#        plt.imshow (rgbImg)
#plt.show()

f = open ('data.pickle', 'wb')
pickle.dump({'data':data, 'labels': labels}, f)
f.close()
