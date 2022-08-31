import cv2
import os
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template

# UPLOAD_FOLDER = 'C:/Users/pwbry/OneDrive/Desktop/Documents/Projects/SketchGeneratorPy/static/uploads'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)                       # Define flask app
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Remove file from the cashe after each use
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Default upload folder
app.secret_key = "secret key"               # A not very secret key

# Check if the uploaded file uses an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to take an image and convert it to a sketch
def make_sketch(image):
    grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                     # Convert the image to greyscale using OpenCV
    inverted = cv2.bitwise_not(grayed)                                   # Invert the greyscale image (black becomes white and vice versa)
    blurred = cv2.GaussianBlur(inverted, (19, 19), sigmaX =0, sigmaY =0) # Blur the inverted image using a Gaussian filter
    final_result = cv2.divide(grayed, 255 - blurred, scale  =256)        # Blend the grayscale image with the blurred inverted image
    return final_result

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Upload page
@app.route('/sketch',methods=['POST'])
def sketch():
    file = request.files['file']                                       # Get the file from the request
    if file and allowed_file(file.filename):                           # Check if the file is valid
        filename = secure_filename(file.filename)                      # Get the filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Save the file to the upload folder
        img = cv2.imread(UPLOAD_FOLDER+'/'+filename)                   # Read the image using OpenCV
        sketch_img = make_sketch(img)                                  # Convert the image to a sketch
        sketch_img_name = filename.split('.')[0]+"_sketch.jpg"         # Create a name for the sketch image
        _ = cv2.imwrite(UPLOAD_FOLDER+'/'+sketch_img_name, sketch_img) # Save the sketch image to the upload folder
        return render_template('home.html',org_img_name=filename,sketch_img_name=sketch_img_name) # Render the home page with the original and sketch images

if __name__ == '__main__':
    app.run(debug = True)
