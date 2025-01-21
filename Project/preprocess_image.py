import numpy as np


def grey_level(arr):
    return ((arr[:,:,0] + arr[:,:,1] + arr[:,:,2])/3).astype(int)

def crop(arr, k=2):
    # Crop an image
    n,m = arr.shape
    x, X, y, Y = n, 0, m, 0
    for i in range(n):
        for j in range(m):
            if arr[i,j]!=1:
                x = min(x, i)
                X = max(X, i)
                y = min(y, j)
                Y = max(Y, j)
    
    return arr[max(x-k,0):min(X+k,n), max(y-k,0):min(Y+k,m)]


def unblur_rgb_arr(arr, size=20):
    # Unblur an RBG image
    def gaussian_grow(kernel):
        s = kernel.shape
        res = np.zeros((s[0]+1,s[1]+1))
        res[:-1,:-1] = kernel
        res[1: ,:-1] += kernel
        res[:, 1:] += res[:, :-1]
        return res

    def gaussian_kernel(size):
        g = np.ones((1,1))
        for _ in range(size-1):
            g = gaussian_grow(g)
        return g

    def img_pad(img, padl, padc = None):
        if padc is None:
            padc = padl
        return np.pad(img, [(padl,padl),(padc,padc),*[(0,0) for _ in img.shape[2:]]], mode='edge')

    def apply_kernel(img, kernel):
        sk = kernel.shape
        ps = [int(s/2) for s in sk]
        si = img.shape
        padded_image = img_pad(img, ps[0], ps[1])
        res = np.zeros(img.shape)
        for i in range(sk[0]):
            for j in range(sk[1]):
                res += kernel[sk[0]-i-1,sk[1]-j-1] * padded_image[i:i+si[0],j:j+si[1]]
        return res

    kernel = gaussian_kernel(size) #smooth the image
    kernel /= np.sum(kernel)
    identity = np.zeros((size,size))
    identity[1,1] = 1 #identity filter, doing nothing
    details = identity - kernel #details : substracting the smoothed image from the original image
    kernel = identity + size*details #emphasizing the details

    arr_sharp = np.clip(apply_kernel(arr, kernel), 0, 1)
    return arr_sharp

def img_to_array(img):
    # Convert an image to an numpy array
    arr = np.array(img)
    return arr

def preprocess_image(img, unblur_size=15, crop_size=2):
     # preprocess an image from an image (from an hugging face dataset for example)
     arr = img_to_array(img)
     arr = unblur_rgb_arr(arr, size=unblur_size)
     #img = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
     #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     arr = grey_level(arr)
     arr = crop(arr, k=crop_size)
     return arr
