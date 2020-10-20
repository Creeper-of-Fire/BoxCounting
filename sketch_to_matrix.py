import cv2.cv2 as cv

def sketch(pic = '1.png'):
    img = cv.imread('../example/'+pic, cv.IMREAD_GRAYSCALE)
    ret_thre1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,37,0)
    #sketch = ret_thre1[-1]
    #sketch.tolist()
    #return sketch
    return ret_thre1
