# Code Adapted from - https://github.com/sleepokay/mnist-flask-app/blob/master/app.py

# Imports
from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import base64


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/', methods=['GET','POST'])
def predict():
    # get data from drawing canvas and save as image
    parseImage(request.get_data())

    # read parsed image back in 8-bit, black and white mode (L)
    x = imread('image.png', mode='L')
    x = np.invert(x)
    x = imresize(x,(28,28))

    # reshape image data for use in neural network
    x = x.reshape(1,28,28,1)

    # load model to predict number
    model = keras.models.load_model("trainedmodel/mnist_model.h5")
    out = model.predict(x)
    print(out)
    #print(np.argmax(out, axis=1))
    response = np.array_str(np.argmax(out, axis=1))
    return response 

def parseImage(imgData):
    # parse canvas bytes and save as image.png
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('image.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

if __name__ == '__main__':
    app.run(debug = True)