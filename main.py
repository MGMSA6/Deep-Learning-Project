# Deep Learning End To End Project

# 1. Create VGG19 Model for classifying imagenet image
# 2. Will create flask app to upload images(Simple html)
# 3. Predict from the flask app with the images that you upload

# import libraries
from tensorflow.keras.applications.vgg19 import VGG19

# define model
model = VGG19(weights="imagenet")

model.save('vgg19.h5')
