# SketchGeneratorPy: https://sketch-generator-py.herokuapp.com/
A very straightforward web-application that allows a user to upload a png, jpg, or jpeg image file and return a "sketched" version of the image. The application is built using Flask and utilizes the Opencv open source library to manipulate the user-inputted image. To create the sketch, Opencv is used to,
<ol>
  <li>Convert the image to greyscale.</li>
  <li>Invert the bits in the greyscale image.</li>
  <li>Apply a Gaussian filter.</li>
  <li>Blend the greyscale image with the blurred image.</li>
</ol>

A sample output of running the application can be seen below.

![demo image](https://github.com/peter-w-bryant/SketchGeneratorPy/blob/main/demo.png)

The web-application is currently being hosted on Heroku, and can be accessed here: https://sketch-generator-py.herokuapp.com/

<h4>Running SketchGeneratorPy Locally</h4>

<p>Clone my repository</p>

```python
$ git clone https://github.com/peter-w-bryant/SketchGeneratorPy.git
```
<p>Create + activate virtual environment</p>

```python
$ python -m venv ./env
$ env/Scripts/activate
```
<p>Install all dependencies</p>

```python
$ pip install -r requirements.txt
```

<p>Run the app and start your local server</p>

```python
$ python app.py
```
