import cv2
import numpy as np

img = cv2.imread('./images/moon_gray.jpg')

k = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)

merged = np.hstack((img, tophat, blackhat))
cv2.imshow('tophat blackhat', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# tophat 그레이디언트 연산과 비슷하게 입력 이미지에 열림 연산을 적용한 이미지를 감산한다.
# blackhat 탑햇 연산과 비슷하게 닫힘 연산을 적용한 이미지에 입력 이미지를 감산한다.
