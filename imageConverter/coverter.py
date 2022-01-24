import cv2

# Reading image
path = r'E:\KodeProsjekter\python-projects\imageConverter\images\me.jpg'
image = cv2.imread(path)

# Converting RGB image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Image inversion
inverted_image = 255 - gray_image

# Creating the pencil sketch
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Displaying the sketch
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of Me", pencil_sketch)
cv2.waitKey(0)

#closing all open windows 
cv2.destroyAllWindows() 