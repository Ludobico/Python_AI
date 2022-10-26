import cv2
import numpy as np
# 코너 검출
# 영상이나 이미지에서 코너를 검출하는 알고리즘이다.

img = cv2.imread('./images/coffee.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corner = cv2.cornerHarris(gray, 2, 3, 0.04)
coord = np.where(corner > 0.1 * corner.max())
coord = np.stack((coord[1], coord[0]), axis=-1)
for x, y in coord:
    cv2.circle(img, (x, y), 5, (0, 0, 255), 1, cv2.LINE_AA)
corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)
merged = np.hstack((corner_norm, img))
merged_re = cv2.resize(merged, dsize=(0, 0), fx=0.3,
                       fy=0.3, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Harris Corner', merged_re)
cv2.waitKey()
cv2.destroyAllWindows()
