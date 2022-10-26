from turtle import shape
import cv2
import numpy as np
# 두 개의 컨투어로 도형 매칭
# 값이 0에 가까울수록 닮음

target = cv2.imread('./images/4star.jpg')
shapes = cv2.imread('./images/shapestomatch.jpg')

targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)

ret, targetTH = cv2.threshold(targetGray, 127, 255, cv2.THRESH_BINARY_INV)
ret, shapesTH = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY_INV)

cntrs_target, _ = cv2.findContours(
    targetTH, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntrs_shapes, _ = cv2.findContours(
    shapesTH, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

matchs = []

for contr in cntrs_shapes:
    match = cv2.matchShapes(cntrs_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
    matchs.append((match, contr))
    cv2.putText(shapes, '%.2f' % match, tuple(
        contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
matchs.sort(key=lambda x: x[0])
cv2.drawContours(shapes, [matchs[0][1]], -1, (0, 255, 0), 3)
cv2.imshow('target', target)
cv2.imshow('Match Shape', shapes)
cv2.waitKey()
cv2.destroyAllWindows()
