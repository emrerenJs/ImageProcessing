import numpy as np

class Basics:
    def info_about_cv2(self):
        print("image[satir,sutun,kanal] değerinde satir-> dikey eksen, sutun->yatay ekseni temsil eder.\n"
              " kanal ise, resim RGB imaj olmak üzere [Blue,Green,Red] değerini barındırır.")

    def copy_image_inside_an_image(self,image1,image2):
        '''
        Bir resim içerisine ikinci resmi kopyalar.
        :param image1: cv2 ile okunmuş 1. resim dosyası
        :param image2: cv2 ile okunmuş 2. resim dosyası
        Resimlerin hangisinin büyük olduğu karşılaştırılır ve büyük olanın içine küçük kopyalanır.
        Resimler aynı boyutta ise image1 arkaplan olarak alınacaktır.
        :return: New Image or False
        '''
        y_1,x_1 = image1.shape[:2]
        y_2,x_2 = image2.shape[:2]
        bg_image = None
        f_image = None
        if(y_1 >= y_2):
            if(x_1 >= x_2):
                bg_image = image1.copy()
                f_image = image2.copy()
            else:
                raise IndexError("Resim boyutları uygun değil!")
        else:
            if(x_2 >= x_1):
                bg_image = image2.copy()
                f_image = image1.copy()
            else:
                raise IndexError("Resim boyutları uygun değil")
        bg_image[:f_image.shape[0],:f_image.shape[1]] = f_image
        return bg_image

    def rgb_random_image(self,h,w):
        '''
        Rastsal olarak değerler oluşturur ve bu değerleri resim formatında geri döner.
        :param h: Görüntü matrisi yüksekliği
        :param w: Görüntü matrisi genişliği
        :return: Görüntü matrisi
        '''
        image = np.random.randint(256, size = (h,w,3),dtype=np.uint8)
        return image

    def crop_image(self,image,y,x,h,w):
        '''
        Resim formatındaki veriden parça kopartır. Parametreler girilirken yükseklik ve genişlik değerinin
        matematiksel olarak mantıklı değerler olması gerekir.
        :param image: Resim formatındaki veri. (cv2 ile okunmuş resim örn.)
        :param x: Yatay başlangıç koordinatı
        :param y: Dikey başlangıç koordinatı
        :param w: Kesme genişliği
        :param h: Kesme yüksekliği
        :return: Kesilmiş resim formatı
        '''
        y_len,x_len = image.shape[:2]
        if(w > x_len or h > y_len):
            raise IndexError("Kesmek istediğiniz parça ana resimden büyük!")
        if(x + w > x_len):
            x -= (x+w) - x_len
        if(y + h > y_len):
            y -= (y + h) - y_len
        cropped = image[y:y+h,x:x+w].copy()
        return cropped

    def reverse_image_vertical(self,image):
        '''
        Resim formatındaki veriyi dikey olarak ters çevirir
        :param image: Resim formatındaki veri. (cv2 ile okunmuş resim örn.)
        :return: Ters çevrilmiş resim formatı
        '''
        img = image.copy()
        img = img[::-1]
        return img
    def reverse_image_horizontal(self,image):
        '''
        Resim formatındaki veriyi yatay olarak ters çevirir
        :param image: Resim formatındaki veri. (cv2 ile okunmuş resim örn.)
        :return: Ters çevrilmiş resim formatı
        '''
        img = image.copy()
        img = img[:, ::-1]
        return img

    def threshold(self,image,threshold):
        '''
        Resim formatındaki veriyi siyah beyaz resme çevirir. Dikkat! Resim Gri olarak okunmalıdır.
        :param image: Resim formatındaki veri. (cv2 ile okunmuş resim örn.)
        :param threshold: Siyah ve beyaz ayrımını yapacak ortalama parlaklık değeri.
        :return: Threshold uygulanmış, siyah beyaz resim
        '''
        if len(image.shape) != 2:
            raise TypeError("Resim gri olmalı!")
        img = image.copy()
        black_index = img < threshold
        img[black_index] = 0
        img[~black_index] = 255
        return img


