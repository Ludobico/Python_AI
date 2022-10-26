import cv2

# 윤곽선(contour) 검출
# 영상이나 이미지의 외곽과 내곽의 윤곽선을 검출하기 위해 사용된다.

src = cv2.imread('./images/contour.png', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)
contoures, hierarchy = cv2.findContours(
    binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
for i in range(len(contoures)):
    cv2.drawContours(src, [contoures[i]], 0, (0, 0, 255), 2)
    cv2.putText(src, str(i), tuple(
        contoures[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow('src', src)
    cv2.waitKey(0)
cv2.destroyAllWindows()
