import numpy as np
import matplotlib.pyplot as plt
from datasets import load_dataset

from preprocess_image import preprocess_image


def plot_img(image, gl=False):
    # plot an image
    # gl=True iff the image is in grey level
    if gl:
        plt.imshow(255-image, cmap="Greys")
    else:
        plt.imshow(image)
    plt.axis("off")
    plt.show()


# Load dataset
ds = load_dataset("OleehyO/latex-formulas", "cleaned_formulas")

train_val_split = ds["train"].train_test_split(test_size=0.2, seed=42)
train_ds = train_val_split["train"]
val_test_split = train_val_split["test"].train_test_split(test_size=0.5, seed=42)
val_ds = val_test_split["train"]
test_ds = val_test_split["test"]

print(train_ds)
print(val_ds)
print(test_ds)

# preprocess an image
row = 3
img = train_ds[row]["image"]
img = preprocess_image(img, do_unblur=True)
plot_img(img, True)

print(train_ds[row]["latex_formula"])