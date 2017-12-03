# Emerging-Technologies-Project
By Donal McGahon - G00299627

## Why I created this application to recognise digits in images
* This was a project given to me for my final year in Software Development in the subject of [Emerging Technologies](https://emerging-technologies.github.io/).
* The project outline was as follows:
In this project you will create a web application in Python to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image. You should use tensorflow and flask to do this. Note that accuracy of approximately 99% is considered excellent in recognising digits, so it is okay if your algorithm gets it wrong sometimes.
* Instructions
1. Create a git repository with a README.md and an appropriate gitignore file. The README should explain who you are, why you created the application, how you created it, how to download and run it, and summarise any references you have used.
1. In the repository, create a web application that serves a HTML page as the root resource. The page should contain an input where the user can upload (or draw) an image containing a digit, and an area to display the image and the digit.
1. Add a route to your application that accepts requests containing a user input image and responds with the digit.
1. Connect the HTML page to the route using AJAX.

## How I created the application
When I looked at the [Instructions](https://emerging-technologies.github.io/problems/project.html) for this project I first looked at creating the single web app using [flask](http://flask.pocoo.org/docs/0.12/quickstart/).
I followed the following [tutorial](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/) for allowing the user to upload an image to the web app.
I successfully got this working, with the image being displayed onto the web app.

But after I done more reseaching on the topic, I found that maybe it would be more beneficial for me to allow the user to draw on a canvas, any digit they would like.
The reason for this change of heart was because I could then have all images for the app the same size of 28x28px. I wanted the images 28x28px because my application was going to be trained to predict images of this size.

I found how to created a simple [canvas](https://www.w3schools.com/tags/att_canvas_width.asp) for the user to draw to.
Next I found a [bootstrap example](https://v4-alpha.getbootstrap.com/examples/starter-template/) to make my app look visibly more appealing.

The next step was to find out how to train my app using [Tensorflow](https://www.tensorflow.org/) to recognise digits in the images the user draws.
I read though the documents on the [tensorflow website](https://www.tensorflow.org/get_started/mnist/pros) which explains using the famous [MNIST dataset](http://yann.lecun.com/exdb/mnist/) to train your application to recognise digits.
So, from a previous assignment we done for our course, we were taught about using Keras to train our dataset. I done some research and found this [keras example](https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py) which uses keras to train the MNIST dataset.
I adapted this code into my application to train it and from my [previous assignment](https://github.com/DonalMcGahon/Tensorflow/blob/master/Tensorflow.ipynb) I knew how to save this trained data and use it again.

I then found an [example](https://github.com/sleepokay/mnist-flask-app/blob/master/app.py) which helped me understand how to read in the trained data and using it in my flask web app.
I adapted this code for use in my [flask python file](https://github.com/DonalMcGahon/Emerging-Technologies-Project/blob/master/digitImageReader.py).

We were then requied to connect our HTML page to the route using AJAX. I then read up on AJAX and in simple terms it just allows you to update a web page without reloading the page.
In the same [example](https://github.com/sleepokay/mnist-flask-app/blob/master/templates/index.html) as above I found out how they used AJAX to update a web page and adapted this example into my flask web app.

So, with my application trained up using the MNIST dataset, my python flask app using the trained data,
my index.html allowing the user to draw an image on a canvas and AJAX updating the predicted digit, my flask app was now functioning correctly.

## How to download and run my application

1. Download zip of repository or clone the repository.
1. Unzip folder or clone in a suitable location for you.
1. Open your cmd on your machine.
1. cd to the repository.
1. Run the following code when you are in the repository `python digitImageReader.py` to run flask app
1. Open your favourite browser and enter `http://127.0.0.1:5000/`

* If you would like to train the data yourself you can do so by following these instructions:
1. Download zip of repository or clone the repository.
1. Unzip folder or clone in a suitable location for you.
1. Open your cmd on your machine.
1. cd to the repository.
1. cd to trainedmodel.
1. Run the following code when you are in the trainedmodel folder `python trainingData.py`
Depending on your machine capabilities this may take some time.
Once trained the trained model file will save in the repository as `trainedmodel.h5` 

## References

#### Where all these references were used in the development of my single page web application are explained in the "How I created the application" section of this README.

Flask - [Reference 1](http://flask.pocoo.org/ ) [Reference 2](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/)

Tensorflow - [Reference 1](https://www.tensorflow.org/) [Reference 2](https://www.tensorflow.org/get_started/mnist/pros)

Keras training model - [Reference](https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py)

AJAX - [Reference]()

Bootstrap - [Reference](https://v4-alpha.getbootstrap.com/examples/starter-template/)

Project which helped me - [Reference](https://github.com/sleepokay/mnist-flask-app)

Canvas - [Reference](https://www.w3schools.com/tags/att_canvas_width.asp)

Previous Assignment - [Reference](https://github.com/DonalMcGahon/Tensorflow/blob/master/Tensorflow.ipynb)

## Accuracy & Loss of Model

| Accuracy| Loss           | 
| ------------- |:-------------:| 
| 99.06% | 0.029%| 
|0.9906   | 0.029336262507|

## Machine-Learning ![machine-learning](https://user-images.githubusercontent.com/14197773/33525295-b44b7cde-d824-11e7-87a2-797b2f445942.png)

Machine learning is a type of artificial intelligence (AI) that allows software applications to become more accurate in predicting outcomes without being explicitly programmed. The basic premise of machine learning is to build algorithms that can receive input data and use statistical analysis to predict an output value within an acceptable range.

Facebook's News Feed, for example, uses machine learning to personalize each member's feed. If a member frequently stops scrolling to read or "like" a particular friend's posts, the News Feed will start to show more of that friend's activity earlier in the feed [1](http://whatis.techtarget.com/definition/machine-learning). 

## Tensorflow ![tensorflow](https://user-images.githubusercontent.com/14197773/33525374-1862cb72-d826-11e7-9953-5c875985eb19.png)

TensorFlow is an open source software library for numerical computation using data-flow graphs. It was originally developed by the Google Brain Team within Google's Machine Intelligence research organization for machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well [2](https://opensource.com/article/17/11/intro-tensorflow).

TensorFlow doesn't exactly give every developer the ability to harness machine learning, but it does provide both a Python and C/C++ API to link into a developer’s program [3](https://www.computerworlduk.com/open-source/what-is-tensorflow-how-are-businesses-using-it-3658374/).

## Flask

![flask](https://user-images.githubusercontent.com/14197773/33525414-fe48ef18-d826-11e7-9485-e37a9a16d44a.png)

Flask is a web framework. This means flask provides you with tools, libraries and technologies that allow you to build a web application.
This web application can be some web pages, a blog, a wiki or go as big as a web-based calendar application or a commercial website [4](http://pymbook.readthedocs.io/en/latest/flask.html).

#### Simple Flask Web App Setup Example

##### In your python file
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```
##### On your cmd
```
$ pip install Flask
$ FLASK_APP=hello.py flask run
 * Running on http://localhost:5000/
``` 
Reference [5](http://flask.pocoo.org/).

## Keras ![keras](https://user-images.githubusercontent.com/14197773/33525516-f76faea0-d828-11e7-9734-3a95083b8304.png)

Keras is an open source neural network library written in Python. It is capable of running on top of MXNet, Deeplearning4j, Tensorflow, CNTK or Theano [6](https://en.wikipedia.org/wiki/Keras).

Use Keras if you need a deep learning library that:

* Allows for easy and fast prototyping (through user friendliness, modularity, and extensibility).
* Supports both convolutional networks and recurrent networks, as well as combinations of the two.
* Runs seamlessly on CPU and GPU.
Reference [7](https://keras.io/)


## AJAX

## Conclusion