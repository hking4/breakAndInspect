##Reusable model skeleton to be referenced in all scripts needing the trained CNN model

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tensorflow as tf
IMG_SIZE = 50
LR = 1e-3

## Return skeleton for CNN model.
## This should be called anytime the TF model is loaded 
def getTfModel():
    with tf.device('/gpu:0'):
        sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
        #sess = tf.Session()
        tf.reset_default_graph()

        convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input')
        convnet = conv_2d(convnet, 32, 2, activation='relu')
        convnet = max_pool_2d(convnet, 2)
        convnet = conv_2d(convnet, 32, 2, activation='relu')
        convnet = max_pool_2d(convnet, 2)
        convnet = conv_2d(convnet, 32, 2, activation='relu')
        convnet = max_pool_2d(convnet, 2)
        convnet = conv_2d(convnet, 32, 2, activation='relu')
        convnet = max_pool_2d(convnet, 2)
        convnet = conv_2d(convnet, 32, 2, activation='relu')
        convnet = max_pool_2d(convnet, 2)
        convnet = conv_2d(convnet, 32, 2, activation='relu')
        convnet = max_pool_2d(convnet, 2)
        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)
        convnet = fully_connected(convnet, 2, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')
        model = tflearn.DNN(convnet, tensorboard_dir='log')
        return model

## Return image size used in pre-processing
def getImgSize():
    return IMG_SIZE