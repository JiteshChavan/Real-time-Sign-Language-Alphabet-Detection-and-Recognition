import pickle 

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np



dataDict = pickle.load (open('./data.pickle', 'rb'))

data = np.asarray(dataDict['data'])
labels = np.asarray(dataDict['labels'])

xTrain, xTest, yTrain, yTest = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier()


model.fit (xTrain, yTrain)

yPredict = model.predict(xTest)

score = accuracy_score(yPredict, yTest)

print ('{}% of samples were classified correctly !', format (score * 100))


f = open ('model.p', 'wb')
pickle.dump({'model':model}, f)
f.close()
