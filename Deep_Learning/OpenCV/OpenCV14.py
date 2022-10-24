import cv2
import numpy as np
import matplotlib.pylab as plt


# 이진화
# 어느 지점을 기준으로 값이 높거나 낮은 픽셀의 값을 대상으로 특정 수행할 때 사용한다.
# 일반적으로 값이 높거나 낮은 픽셀을 검은색 또는 흰색의 값으로 변경한다.

img = cv2.imread('./images/bird.jpg', cv2.IMREAD_GRAYSCALE)
thresh_np = np.zeros_like(img)
thresh_np[img > 127] = 255

ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(ret)

imgs = {'original': img, 'numpy api': thresh_np, 'cv2.threshold': thresh_cv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]), plt.yticks([])
plt.show()
