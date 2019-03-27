#Convolutional Neural network
#Created on Wed Mar 27 13:51:44 2019

#Importing Keras libs and packages
from keras.models import Sequential
from keras.layers import Convolutional2D
from keras.layers import MaxPoolin2D
from keras.layers import Flatten
from keras.layers import Dense

#Initialize cnn
classifier = Sequential()

#1_convolution
classifier.add(Convololution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

#2_pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

#3_flattening
classifier.add(Flatten())

#4_full connection - connect cnn to NN
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

#cnn compilation
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


#CNN Data Fitting
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range = 0.2,
        horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/training_set', #training images directory
        target_size=(64, 64),
        batch_size = 32,
        class_mode='binary'
)

test_set = test.datagen.flow_from_directory(
        'dataset/test_set', #testing images directory
        target_size(64, 64),
        batch_size=32, 
        class_mode='binary'
)


#####NETWORK TRAINING######
from IPython.display import display
from PIL import Image

classifier.fit_generator(
        training_set,
        steps_per_epoch=8000,
        epochs=10,
        validation_data=test_set,
        validation_steps=800
)



#####NETWORK TESTING#####
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('random.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = no.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] >= 0.5:
    prediction = ''
else:
    prediction = ''
print(prediction)