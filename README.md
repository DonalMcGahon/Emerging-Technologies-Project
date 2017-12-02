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
When I looked at the [Instructions](https://emerging-technologies.github.io/problems/project.html) for this project I first looked at creating the single web app using flask.
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


## How to download and run my application

## Reference Summary

## Machine-Learning

## Tensorflow

## Flask

## Karas

## AJAX

## Conclusion

## References
* Flask simple [project](http://flask.pocoo.org/)
* Flask uploading [files](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/)