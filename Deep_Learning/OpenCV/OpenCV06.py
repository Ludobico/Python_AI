import cv2
import matplotlib.pyplot as plt


def img_show(title='image', img=None, figsize=(8, 5)):
    plt.figure(figsize=figsize)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []

            for i in range(len(img)):
                titles.append(title)
        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()

    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()


src = cv2.imread('./images/cat.jpg', cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)
dst1 = cv2.flip(src, -1)
dst2 = cv2.flip(src, 1)

img_show(['src', 'dst', 'dst1', 'dst2'], [
         src, dst, dst1, dst2], figsize=(12, 5))
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
