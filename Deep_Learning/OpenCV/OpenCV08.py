
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
height, width, channel = src.shape

dst_pyrUp = cv2.pyrUp(src, dstsize=(width * 2, height * 2),
                      borderType=cv2.BORDER_DEFAULT)
dst_pyrdown = cv2.pyrDown(src)

cv2.imshow('src', src)
cv2.imshow('pyrup', dst_pyrUp)
cv2.imshow('pyrdown', dst_pyrdown)
cv2.waitKey()
cv2.destroyAllWindows()
