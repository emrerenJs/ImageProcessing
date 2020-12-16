import numpy as np

class Morphology():
    def __hit(self,array,struct):
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                if struct[i, j] and array[i, j]:
                    return True
        return False

    def __fit(self,array,struct):
        true_false_matrix = np.zeros(array.shape, np.uint8)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                true_false_matrix[i, j] = not (struct[i, j]) or array[i, j]
        return true_false_matrix.all()

    def dilate(self,image,struct,iteration):
        img = image.copy()
        s_y,s_x = struct.shape[:2]
        for i in range(iteration):
            border_indexes = []
            for i in range(image.shape[0] - (s_y - 1)):
                for j in range(image.shape[1] - (s_x - 1)):
                    if self.__hit(image[i:i + s_y, j:j + s_x],struct):
                        border_indexes.append([i + 1, j + 1])
            for i in range(len(border_indexes)):
                y, x = border_indexes[i]
                img[y, x] = 255
        return img

    def erode(self,image,struct,iteration):
        img = image.copy()
        s_y,s_x = struct.shape[:2]
        for i in range(iteration):
            border_indexes = []
            for i in range(image.shape[0] - (s_y - 1)):
                for j in range(image.shape[1] - (s_x - 1)):
                    if not self.__fit(image[i:i + s_y, j:j + s_x],struct):
                        border_indexes.append([i + 1, j + 1])
            for i in range(len(border_indexes)):
                y, x = border_indexes[i]
                img[y, x] = 0
        return img

    def edge_detection(self,image,struct,iteration):
        img = image.copy()
        s_y,s_x = struct.shape[:2]
        for i in range(iteration):
            border_indexes = []
            for i in range(image.shape[0] - (s_y - 1)):
                for j in range(image.shape[1] - (s_x - 1)):
                    if self.__fit(image[i:i + s_y, j:j + s_x],struct):
                        border_indexes.append([i + 1, j + 1])
            for i in range(len(border_indexes)):
                y, x = border_indexes[i]
                img[y, x] = 0
        return img

    def open(self,image,struct,iteration):
        newImage = image
        for i in range(iteration):
            newImage = self.erode(newImage,struct,iteration)
        for i in range(iteration):
            newImage = self.dilate(newImage, struct, iteration)
        return newImage

    def close(self,image,struct,iteration):
        newImage = image
        for i in range(iteration):
            newImage = self.dilate(newImage, struct,iteration)
        for i in range(iteration):
            newImage = self.erode(newImage, struct,iteration)
        return newImage
