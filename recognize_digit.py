import numpy as np
import matplotlib.pyplot as plt
import random as rd
# police des titres
plt.rc('font', family='serif', size='18')
from IPython.display import display,Markdown

import sklearn as sk
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression


# Loading dataset
digits = datasets.load_digits()

# Printing dataset information
display(Markdown(digits.DESCR))
print(type(digits))
print("keys:", digits.keys())

print("Data:",digits.data.shape)
print("Result:",digits.target.shape)

def plot_image(i):
    # Plot a simgle image of the dataset
    plt.imshow(digits.images[i], cmap='binary')
    plt.title(digits.target[i])
    plt.axis('off')
    plt.show()

def plot_data(data,target,pred=None,nmax=64,titre=None):
    '''affiche les 64 premiers elts de la BD'''
    # set up the figure
    fig = plt.figure(figsize=(12, 12))  # figure size 
    if titre is not None: plt.title(titre)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    # plot the digits: each image is 8x8 pixels
    for i in range(nmax):
        ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
        image = data[i].reshape(8,8)
        ax.imshow(image, cmap=plt.cm.binary, interpolation='nearest')    
        # label the image with the target value
        ax.text(0, 7, str(target[i]),color='b')
        # and the predicted value
        if pred is not None: ax.text(7,7, str(pred[i]),color='r')
    plt.show()



random_seed = rd.randint(0,4294967295)
trainning_size = 0.8
# Splitting dataset into 2 parts: trainning and test
res = train_test_split(digits.data, digits.target,
                        train_size=trainning_size, test_size=1-trainning_size,
                        random_state=random_seed)
train_data, test_data, train_labels, test_labels = res

print("dataset training:",train_data.shape)
print("dataset test    :",test_data.shape)

# plot_data(train_data, train_labels, titre="data set d'entrainement")
# plot_data(test_data, test_labels, titre="data set de test")

# normalisation of data
def normalize_array(arr):
    norm_arr = arr
    #norm_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    return norm_arr

X_train = normalize_array(train_data)
y_train = normalize_array(train_labels)
X_test  = normalize_array(test_data)
y_test  = normalize_array(test_labels)

def test_train_test_assert():
    assert (X_train.shape == train_data.shape)
    assert (y_train.shape == train_labels.shape)
    assert (X_test.shape  == test_data.shape)
    assert (y_test.shape  == test_labels.shape)
test_train_test_assert()



def plot_sigmoide():
    Y = np.linspace(-10,10,100)
    plt.title("probabilité Y=1 (sigmoide)")
    plt.plot(Y,1./(1+np.exp(-Y)))
    Y1 = np.linspace(-10,-3,10)
    plt.plot(Y1,np.zeros(10),'or')
    plt.plot(-Y1,np.ones(10),'or')
    plt.xlabel('z(X)')
    plt.show()

model = LogisticRegression(max_iter=200).fit(X_train, y_train)
print("training score:", model.score(X_train, y_train))
print("test score:", model.score(X_test, y_test))
print()

def predict_image(i):
    d = digits.data[i].reshape(1, -1)
    print("guess:", model.predict(d)[0])
    plot_image(i)


def predict_random_images(x):
    for i in range(x):
        predict_image(rd.randint(0, 100))

predict_random_images(10)
