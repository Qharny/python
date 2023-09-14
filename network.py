# Import libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Load the Iris dataset
iris = load_iris()
X = iris.data # Features
y = iris.target # Labels

# Convert labels to one-hot vectors
y = to_categorical(y)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,))) # Hidden layer with 10 neurons
model.add(Dense(3, activation='softmax')) # Output layer with 3 neurons (one for each class)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=32)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print('Test accuracy: {:.2f}%'.format(accuracy * 100))

# Make predictions for some new samples
X_new = np.array([[5.1, 3.5, 1.4, 0.2], # Iris-setosa
                  [6.7, 3.0, 5.2, 2.3], # Iris-virginica
                  [5.9, 3.2, 4.8, 1.8]]) # Iris-versicolor

y_pred = model.predict(X_new)
y_pred_class = np.argmax(y_pred, axis=1)

# Print the predicted class labels
print('Predicted class labels:', y_pred_class)
