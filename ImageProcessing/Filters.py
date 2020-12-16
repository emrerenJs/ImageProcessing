import numpy as np
class Filters():
    def __kernel_avg(self,arr,ks):
        blue_sum = 0
        green_sum = 0
        red_sum = 0
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                blue_sum += arr[i,j,0]
                green_sum += arr[i,j,1]
                red_sum += arr[i,j,2]
        return [blue_sum/ks,green_sum/ks,red_sum/ks]

    def __kernel_med(self,arr,ks):
        blue_vector = []
        green_vector = []
        red_vector = []
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                blue_vector.append(arr[i,j,0])
                green_vector.append(arr[i,j,1])
                red_vector.append(arr[i,j,2])
        blue_vector = np.sort(blue_vector)
        green_vector = np.sort(green_vector)
        red_vector = np.sort(red_vector)
        return [np.mean(blue_vector),np.mean(green_vector),np.mean(red_vector)]


    def blur(self,image,kernel_size):
        if(kernel_size < 1):
            return image
        ks = (2*kernel_size) + 1
        y,x,d = image.shape
        new_image = image.copy()
        for i in range(y - (ks - 1)):
            for j in range(x - (ks - 1)):
                new_image[i + kernel_size, j + kernel_size] = self.__kernel_avg(image[i:i+ks,j:j+ks],ks**2)
        return new_image


    def medianBlur(self,image,kernel_size):
        if (kernel_size < 1):
            return image
        ks = (2 * kernel_size) + 1
        y, x, d = image.shape
        new_image = image.copy()
        for i in range(y - (ks - 1)):
            for j in range(x - (ks - 1)):
                new_image[i + kernel_size, j + kernel_size] = self.__kernel_med(image[i:i + ks, j:j + ks], ks ** 2)
        return new_image
