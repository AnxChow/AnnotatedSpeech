import os
import csv
import pandas as pd
import librosa
import glob
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

def extract_and_process():
    with open("train.csv", "rb") as f:
        reader = csv.reader(f, delimiter=",")
        file_names=[]
        labels=[]
        features=[]
        colNames=next(reader)
        for row in reader:
            file_names.append(row[0])
            labels.append(row[1])
            X, sample_rate = librosa.load(row[0])
            # we extract mfcc feature from data
            mfcc = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
            features.append(mfcc)
    X = np.array(features)
    y = np.array(labels)
    lb = LabelEncoder()
    y = np_utils.to_categorical(lb.fit_transform(y))
    return X,y

def validation_set():
    with open("validate.csv") as f:
        reader = csv.reader(f, delimiter=",")
        file_names=[]
        labels=[]
        features=[]
        colNames=next(reader)
        for row in reader:
            file_names.append(row[0])
            labels.append(row[1])
            X, sample_rate = librosa.load(row[0])
            # we extract mfcc feature from data
            mfcc = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
            features.append(mfcc)
    X = np.array(features)
    y = np.array(labels)
    lb = LabelEncoder()
    y = np_utils.to_categorical(lb.fit_transform(y))
    return X,y


features, labels=extract_and_process()
val_x, val_y = validation_set()

def model(features, labels, val_x, val_y):
    model = Sequential(
    [
        Dense(256, input_shape=(40,)),
        Activation('softmax'),
        Dense(2),
        Activation('softmax'),
    ])
    model.compile(optimizer='adagrad', loss='mean_squared_error', metrics=['accuracy'])
    model.fit(features, labels, batch_size=32, epochs=5, validation_data=(val_x, val_y))

model(features,labels, val_x, val_y)
