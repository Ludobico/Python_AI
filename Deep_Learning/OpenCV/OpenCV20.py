import cv2
import numpy as np
import matplotlib.pyplot as plt
# 가장자리 검출


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


img = cv2.imread('./images/sudoku.jpg')
gx_k = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gy_k = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

img_show(['img', 'edge_gx', 'edge_gy', 'edge_gx+gy'],
         [img, edge_gx, edge_gy, edge_gx + edge_gy])
cv2.waitKey(0)
cv2.destroyAllWindows()
