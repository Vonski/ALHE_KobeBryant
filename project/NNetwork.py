
from keras import regularizers
from keras.models import Sequential
from keras.layers import Activation
from keras.optimizers import SGD
from keras.layers import Dense, Dropout
from keras.utils import np_utils, to_categorical
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.rcParams['figure.figsize'] = [7.5,14]

class NNetwork:

    def __init__(self,data="../data/data.csv"):
        self.prepareData(data)
        self.generateAdditionalPoints()
        self.shuffleData()
        self.buildModel()

    def prepareData(self, data):
        # wczytaj dane i odrzuć wiersze, w których występuje NaN (nie ma shot_made_flag)
        data=pd.read_csv(data)
        data.dropna(inplace=True)
        X = data[["loc_x", "loc_y"]]
        y = data[["shot_made_flag"]]
        self.x_data=np.array(X)
        self.y_data=np.array(y)
        self.X = np.array(X)
        self.Y = to_categorical(np.array(y))

    def generateAdditionalPoints(self):
        cnt_lr = 2000
        cnt_ud=1000
        additional_points_1 = np.concatenate((np.random.randint(-350, 350, (cnt_ud,1)), np.random.randint(-100, -50, (cnt_ud,1))), axis=1)
        additional_points_2 = np.concatenate((np.random.randint(-350, 350, (cnt_ud,1)), np.random.randint(750, 800, (cnt_ud,1))), axis=1)
        additional_points_3 = np.concatenate((np.random.randint(-350, -300, (cnt_lr,1)), np.random.randint(-50, 800, (cnt_lr,1))), axis=1)
        additional_points_4 = np.concatenate((np.random.randint(300, 350, (cnt_lr,1)), np.random.randint(-50, 800, (cnt_lr,1))), axis=1)
        additional_y = np.array([[1.0,0.0]]*(cnt_ud*2+cnt_lr*2))
        self.X = np.concatenate((self.X, additional_points_1, additional_points_2, additional_points_3, additional_points_4))
        self.Y = np.concatenate((self.Y, additional_y))

    def shuffleData(self):
        p = np.random.permutation(len(self.Y))
        self.X = self.X[p]
        self.Y = self.Y[p]

    def buildModel(self):
        self.model = Sequential()
        self.model.add(Dense(100, input_dim=2, activation="relu"))#, kernel_regularizer=regularizers.l2(0.01)))
        self.model.add(Dense(100, input_dim=2, activation="relu"))#, kernel_regularizer=regularizers.l2(0.01)))
        self.model.add(Dense(2, activation="softmax"))
        
    def train(self):
        self.model.compile(loss="binary_crossentropy", optimizer="Adam", metrics=["accuracy"])
        self.model.fit(self.X, self.Y, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

    def predict(self, x):
        return self.model.predict(np.array(x))

    def plotBoundary(self,pred_func):
        # Set min and max values and give it some padding
        x_min = -300
        x_max = 300
        y_min = -100
        y_max = 800
        h = 1
        # Generate a grid of points with distance h between them
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        # Predict the function value for the whole gid
        Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
        Z = Z[:,0].reshape(xx.shape)
        # Plot the contour and training examples
        cs = plt.contourf(xx, yy, Z, 50, cmap=plt.cm.Spectral)
        plt.colorbar(cs)
        plt.show()

    def generateMeshgrid(self):
        x_min = -300
        x_max = 300
        y_min = -100
        y_max = 800
        h = 1
        x,y=np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        z= np.c_[x.ravel(), y.ravel()]
        print(z)
        return z


