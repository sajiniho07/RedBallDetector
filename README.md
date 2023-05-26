# Circle Detection using OpenCV

This code demonstrates circle detection in an image using OpenCV. The code reads an image file and performs the following steps:

- Convert the image from BGR (default color space in OpenCV) to HSV
- Convert the HSV image to grayscale
- Detect circles using HoughCircles function of OpenCV
- Draw the detected circles on the original image
- Identify red colored circles by checking the color values of a small portion of the image around the center of each detected circle
- Display the number of detected circles and their locations (if red colored)

## Example Output
```
Red circle center location(x, y) is: (148, 78)
Detected Circles Count: 12
```

![sample](https://github.com/sajiniho07/RedBallDetector/blob/master/res/output-sample.png)

## Requirements ##

- Python 3.x
- OpenCV
- NumPy

## Usage ##
1- Clone or download this repository

2- Provide the image path in the img variable

3- Run the code using python project.py

## License ##

Made with :heart: by <a href="https://github.com/sajiniho07" target="_blank">Sajad Kamali</a>

<a href="#top">Back to top</a>
