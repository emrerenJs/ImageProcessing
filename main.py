from ImageProcessing import Basics as basics, Morphology as morphology, Filters as filters, Histogram as histogram
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2
import random


def program():
    _morph = morphology.Morphology()
    _basics = basics.Basics()
    _filters = filters.Filters()
    _histogram = histogram.Histogram()

    image = cv2.imread("./Images/kizkulesi.jpg")
    image2 = cv2.imread("./Images/kizkulesi.jpg")
    image2 = _filters.blur(image2,1)

    print(ssim(image,image2,multichannel=True))

def test():
    pass


if __name__ == "__main__":
    program()
    test()