# Code Adapted from - https://github.com/sleepokay/mnist-flask-app/blob/master/app.py
# Imports
from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import base64

# Created an instance of the Flask class for my web app
app = Flask(__name__)

# Home route, bring user to main page which is index.html in the templates folder
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict/', methods=['GET','POST'])
def predict():
    # get data from drawing canvas and save as image
    parseImage(request.get_data())

    # read parsed image back in 8-bit, black and white mode (L)
    x = imread('static/image.jpg', mode='L')
    x = np.invert(x)
    x = imresize(x,(28,28))

    # reshape image data for use in neural network
    x = x.reshape(1,28,28,1)

    # This loads model to predict number in the image. I created this by running the trainingData.py file
    model = keras.models.load_model("trainedmodel/trainedmodel.h5")
    # out predicts what the number in the image is, the image is (x) which has been reshaped into 28x28px
    out = model.predict(x)
    print(out)
    # response turns the image number to the predicted string value
    response = np.array_str(np.argmax(out, axis=1))
    print(response)
    # Return the predicted response
    return response


def parseImage(imgData):
    # parse canvas bytes and save as image.jpg
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('static/image.jpg','wb') as output:
        output.write(base64.decodebytes(imgstr))

if __name__ == '__main__':
    app.run(debug = True)