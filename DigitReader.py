import os
from flask import send_from_directory
from flask import Flask, request, redirect, url_for, send_from_directory
from flask import render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Creating file path for images
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Home route, bring user to main page
@app.route("/")
def index():
    return render_template("home.html")


@app.route("/upload", methods=["POST"])
def upload():
    # Created a variable called target, that creates a folder where the files will be stored
    target = os.path.join(APP_ROOT, 'images/')
    # If there isn't a folder created, then create it
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))

    # Loop through files
    for upload in request.files.getlist("file"):
        # Update filename from the list
        filename = upload.filename
        # Tell the server to save this file with this name to this destination
        destination = "/".join([target, filename])
        # Save file to destination
        upload.save(destination)

    return render_template("home.html", image_name=filename)    
    

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

# Run app
if __name__ == "__main__":
    app.run(debug=True)