class ComponentLabelling():
    def __scan_ccl_table(self,array,Q):
        minValue = Q
        boolygooly = True
        for i in range(3):
            for j in range(3):
                if(array[i,j] > 0 and array[i,j] < minValue):
                    minValue = array[i,j]
                    boolygooly = False
        array[1,1] = minValue
        return boolygooly

    def connected_component_labelling(self,image):
        Q = 1
        table = {}
        y,x = image.shape[:2]
        labelled_image = image.copy()
        for i in range(y):
            for j in range(x):
                if labelled_image[i+1,j+1] != 0:
                    isQchanged = self.__scan_ccl_table(labelled_image[i:i+3,j:j+3],Q)
                    Q = Q + 1 if isQchanged else Q