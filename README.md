# SketchGeneratorPy
A very straightforward web-application that allows a user to upload a png, jpg, or jpeg image file and return a "sketched" version of the image. The application is built using Flask and utilizes the Opencv open source library to manipulate the user-inputted image. To create the sketch, Opencv is used to,
<ol>
Convert the image to greyscale.
Invert the bits in the greyscale image.
Apply a Gaussian filter.
Blend the greyscale image with the blurred image.
</ol>


![demo image](https://github.com/peter-w-bryant/SketchGeneratorPy/blob/main/demo.png)

The application is built using Flask and utilizes the Opencv open source library to manipulate the user inputted image. 



