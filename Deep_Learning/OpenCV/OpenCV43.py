import cv2

# 템플릿 매칭
# 원본 이미지에서 템플릿 이미지와 일치하는 영역을 찾는 알고리즘이다.

src = cv2.imread('./images/hats.png', cv2.IMREAD_GRAYSCALE)
templit = cv2.imread('./images/hat.png', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('./images/hats.png')
result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)

minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)

x, y = minloc
h, w = templit.shape

dst = cv2.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 1)
dst_re = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5,
                    interpolation=cv2.INTER_LINEAR)

cv2.imshow('dst', dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()
