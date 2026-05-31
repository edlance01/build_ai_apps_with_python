import tensorflow as tf
import keras
from keras import layers
import numpy as np

# Load the MNIST dataset (70,000 handwritten digit images, split into train and test sets)
# x = images (28x28 pixel arrays), y = labels (the actual digit 0-9)
# NOTE - See lab_8_1B_show_images.py to see the actual images
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize pixel values from 0-255 to 0-1
# This helps the model train faster and more consistently
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build a CNN (Convolutional Neural Network) model
model = keras.Sequential(
    [
        # Reshape from (28,28) to (28,28,1) — adds a color channel dimension required by Conv2D
        layers.Reshape((28, 28, 1), input_shape=(28, 28)),
        # First convolutional layer — learns 32 basic features (edges, curves)
        # using a 3x3 filter, relu drops negative values to help the model learn non-linear patterns
        layers.Conv2D(32, (3, 3), activation="relu"),
        # Downsample the image by taking the max value in each 2x2 block
        # Reduces size and computation while keeping the strongest features
        layers.MaxPooling2D((2, 2)),
        # Second convolutional layer — learns 64 more complex features
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        # Flatten the 2D feature maps into a 1D vector so Dense layers can process it
        layers.Flatten(),
        # Fully connected layer — combines all features to start making a decision
        layers.Dense(64, activation="relu"),
        # Output layer — 10 neurons, one per digit (0-9)
        # Softmax converts raw scores into probabilities that sum to 1
        layers.Dense(10, activation="softmax"),
    ]
)

# Configure the training process:
# - adam: an efficient optimizer that adjusts learning rate automatically
# - sparse_categorical_crossentropy: loss function for multi-class classification with integer labels
# - accuracy: metric to track during training
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# Train the model on 60,000 training images for 3 full passes (epochs)
model.fit(x_train, y_train, epochs=3)

# Evaluate performance on the 10,000 test images the model has never seen
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Accuracy:", test_acc)

# Test on a single image (the first image in the test set, which is a 7)
sample = x_test[0]

# model.predict expects a batch, so wrap sample in an array to make it shape (1, 28, 28)
prediction = model.predict(np.array([sample]))

# argmax returns the index (0-9) with the highest probability — that's the predicted digit
print("Predicted digit:", prediction.argmax())
print("Actual label:", y_test[0])
