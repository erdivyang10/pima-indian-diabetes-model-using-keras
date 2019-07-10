#import all libraries

import tensorflow as tf
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense


#load the indian diabeteis data
dataset = loadtxt('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv', delimiter=',')

#split the data into X and Y
X = dataset[:,0:8]
Y = dataset[:,8]

#define the keras models
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1,activation ='sigmoid'))


#Compile the model
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

#fit the keras model on the dataset
model.fit(X,Y, epochs=180, batch_size=10 )

#evaluate the keras model
_,accuracy = model.evaluate(X,Y)
print('Accuracy: %.2f' % (accuracy*100))
predictions = model.predict_classes(X)


# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], Y[i]))
