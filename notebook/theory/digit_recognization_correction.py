import sklearn as sk
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random as rd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='serif', size='18') # For title policy

digits = datasets.load_digits()
print(digits.keys())

def show_image(i):
    # plot the i-th image of the database
    plt.imshow(digits.images[i],cmap='binary')
    plt.title(digits.target[i])
    plt.axis('off')
    plt.show()


random_seed = rd.randint(0,4294967295) # Random seed to split the database with random part
trainning_size = 0.8 # To have 80% of the database for trainning
# Splitting dataset into 2 parts: trainning and test
res = train_test_split(digits.data,
                        digits.target,
                        train_size=trainning_size,
                        test_size=1-trainning_size,
                        random_state=random_seed)
train_data, test_data, train_labels, test_labels = res

# Create the model
model = LogisticRegression(max_iter=200)

# Train the model with the train_data
model.fit(train_data, train_labels)

# Print the score
print("Training score:", model.score(train_data, train_labels))
print("Test score:    ", model.score(test_data, test_labels))

def show_errors():
    errors = []
    for i in range(len(test_data)):
        result = model.predict([test_data[i]])[0]
        if result != test_labels[i]:
            print("model guess", result, "but correct answer was", test_labels[i])
            errors.append(test_labels[i])

    arr = np.array(errors)-0.25 # applying -0.25 to each errors so that the histogram his align with the integer
    plt.hist(arr, color='orange', edgecolor='black') # Create histogram bars
    plt.xticks(range(10)) # ploting every interger in x axis
    plt.xlabel("digits")
    plt.ylabel("number of errors")
    plt.show()

