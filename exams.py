import cv2
import numpy as np
from ImageProcessing import Morphology as morphology

def pepper_n_salt():
    img = cv2.imread("./Images/kizkulesi.jpg",0)
    s_vs_p = 0.5
    y,x = img.shape
    amount = 0.2
    new_image = img.copy()
    #tuz
    num_salt = np.ceil(amount * img.size * s_vs_p)
    salt_coords = [np.random.randint(0, i - 1,int(num_salt)) for i in img.shape]
    new_image[salt_coords[0],salt_coords[1]] = 255
    #pepper
    num_pepper = np.ceil(amount * img.size * (1 - s_vs_p))
    pepper_coords = [np.random.randint(0, i - 1,int(num_pepper)) for i in img.shape]
    new_image[pepper_coords[0],pepper_coords[1]] = 0

    print(len(salt_coords[0]))

    cv2.imshow("xd", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def _sifre_uygula(image,word):
    counter = 0
    for i in range(len(word)):
        image[i,i] = ord(word[i:i+1])
        counter +=1
    image[counter,counter] = ord("`")

def _sifre_coz(image):
    counter = 0
    output = ""
    while(counter < image.shape[0] or counter < image.shape[1]):
        if(chr(image[counter,counter]) == "`"):
            break
        output += chr(image[counter,counter])
        counter += 1
    print(output)

def steganography():
    image = cv2.imread("./Images/jerry.png",0)
    word = "bilgisayar"
    _sifre_uygula(image,word)
    cv2.imshow("xd",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    _sifre_coz(image)

def find_binary_image():
    image = cv2.imread("./Images/jerry.png",0)
    max = image[0, 0]
    min = image[0, 0]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if (max < image[i][j]):
                max = image[i][j]
            if (min > image[i][j]):
                min = image[i][j]

    threshold = int((max + min) / 2)
    black_index = image < threshold
    image[black_index] = 0
    image[~black_index] = 255
    """
    _morph = morphology.Morphology()
    image = _morph.erode(image,np.array([[0,1,0],[1,1,1],[0,1,0]],np.uint8),1)
    """
    cv2.imshow("im",image)
    cv2.imwrite("./ProcessedImages/jerry2.png",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def _get_confusion_matrix(gt_image,image):
    TP,TN,FP,FN = 0,0,0,0
    for i in range(gt_image.shape[0]):
        for j in range(gt_image.shape[1]):
            if(gt_image[i,j] == 0 and image[i,j] == 0):
                TN += 1
            elif(gt_image[i,j] == 255 and image[i,j] == 255):
                TP += 1
            elif(gt_image[i,j] == 255 and image[i,j] == 0):
                FN += 1
            else:
                FP += 1
    return {
        "TP" : TP,
        "TN" : TN,
        "FP" : FP,
        "FN" : FN
    }


def algoritma_test():
    gt_image = cv2.imread("./ProcessedImages/jerry.png",0)
    image = cv2.imread("./ProcessedImages/jerry2.png",0)
    cf_matrix = _get_confusion_matrix(gt_image,image)
    return (cf_matrix["TN"] + cf_matrix["TP"])/(cf_matrix["TN"] + cf_matrix["TP"] + cf_matrix["FP"] + cf_matrix["FN"])

print(algoritma_test())