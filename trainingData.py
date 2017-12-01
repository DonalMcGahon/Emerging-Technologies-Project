# Code adapted from - https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py
# Reference - https://elitedatascience.com/keras-tutorial-deep-learning-in-python helped me understand what was happening in this code and helped me comment the code.
# Imports
import keras 
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

# Number of samples used
batch_size = 128
# Number of binary numbers used. We have 10 different inputs from 0 - 9 so there is 10 binary numbers, one for each
num_classes = 10
# The number of times it goes through the data set
epochs = 12

# input image dimensions
img_rows, img_cols = 28, 28

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# If statement decides how image data is going to be displayed.
# If its the channels_first then it will be channel, img_rows and img_cols
# Otherwise it will be img_rows, img_cols and channel
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

# Setting x_test & x_train to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# This normalize's our data values to the range [0, 1]
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)

# Simply printing the amount of train and test samples
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# Declaring a sequential model format. You can add layers to the model by using the add method.
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), # These correspond to the number of convolution filters to use, the number of rows in each convolution kernel, and the number of columns in each convolution kernel, respectively.
                activation='relu',# Activation Function
                input_shape=input_shape))# This is the shape which corresponds to  the (depth, width, height) of each digit image.

# Adds a convolution layer that has filters, kernal_size and a activation function
model.add(Conv2D(64, (3, 3), activation='relu'))
# MaxPooling2D is a way to reduce the number of parameters in our model by sliding a 2x2 pooling filter across the previous layer and taking the max of the 4 values in the 2x2 filter.
model.add(MaxPooling2D(pool_size=(2, 2)))
# This is a method for regularizing our model in order to prevent overfitting.
model.add(Dropout(0.25))

# For Dense layers, the first parameter is the output size of the layer. Keras automatically handles the connections between layers.
model.add(Flatten())
model.add(Dense(128, activation='relu'))
# This is a method for regularizing our model in order to prevent overfitting.
model.add(Dropout(0.5))
# Final dense has num_classes which is 10 for the amount of digits 0-9 
model.add(Dense(num_classes, activation='softmax'))
# The model compiles with functions loss, optimizer and metrics
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# This fits the model. It declares the batch_size and the number of epochs to train for. validation_data evaluates the loss and any model metrics at the end of each epoch.
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs, 
          verbose=1,
          validation_data=(x_test, y_test))

# Calculates our loss and accuracy
score = model.evaluate(x_test, y_test, verbose=0)

# Prints out loss
print('Test loss:', score[0])
# Prints out accuracy
print('Test accuracy:', score[1])

# Saves model
model.save("mnist_model.h5")