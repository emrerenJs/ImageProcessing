import numpy as np
class Histogram():
    def histogram_equalization(self,image):
        equalized_image = image.copy()
        frequencies = []
        