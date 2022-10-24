import cv2

# 적응형 이진화
# 적응형 이진화 알고리즘은 입력 이미지에 따라 임계값이 스스로 다른 값을 할당할 수 있도록
# 구성된 이진화 알고리즘이다.

src = cv2.imread('./images/bigdata.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 467, 37)
binary_re = cv2.resize(binary, dsize=(0, 0), fx=0.7,
                       fy=0.7, interpolation=cv2.INTER_LINEAR)


height, width = binary.shape
dst_pyrUp = cv2.pyrUp(binary, dstsize=(width * 2, height * 2),
                      borderType=cv2.BORDER_DEFAULT)

cv2.imshow("binary dst_pyrUp", dst_pyrUp)
cv2.waitKey(0)
cv2.destroyAllWindows()
