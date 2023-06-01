"""
    A simple neural network written in Keras (TensorFlow backend) to classify the IRIS data
"""

import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import layers

iris_data = load_breast_cancer() # load the iris dataset

x = irisdata.data
y = iris_data.target.reshape(-1, 1) # Convert data to a single column

# One Hot encode the class labels
encoder = OneHotEncoder(sparse=False)
y = encoder.fittransform(y)
#print(y)

# Split the data for training and testing
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.30)

# Build the model

model = Sequential()

# Adding the input layer and the first hidden layer
model.add(Dense(16, activation='relu', input_dim=30, name='layer1'))


# Adding the second hidden layer
model.add(Dense(16, activation='relu', name='layer2'))

# Adding the output layer (output_dim is 1 as we want only 1 output from the final layer.)
model.add(Dense(2, activation='softmax', name='output'))

# Adam optimizer with learning rate of 0.001
optimizer = Adam(lr=0.001)
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

print('Neural Network: ')
print(model.summary())

# Train the model
model.fit(train_x, train_y, verbose=2, epochs=398)

# Test on unseen data

results = model.evaluate(test_x, test_y)

print('Final loss: {:4f}'.format(results[0]))
print('Final accuracy: {:4f}'.format(results[1]))
