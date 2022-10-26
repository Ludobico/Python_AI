import cv2

# 트랙바
# 스크롤 바의 하나로, 슬라이더 바의 형태를 갖고 있다.
# 트랙 바는 일정 범위 내의 값을 변경할 때 사용하며, 적절한 임곗값을 찾거나 변경하기 위해 사용한다.
# opcnCV의 트랙 바는 생성된 윈도우 창에 트랙바를 부착해 사용할 수 있다.


def onChange(pos):
    print(pos)


src = cv2.imread('./images/cherryblossom.jpg', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('TrackBar windows')
cv2.createTrackbar('threshold', 'TrackBar windows', 0, 255, onChange)
cv2.createTrackbar('maxValue', 'TrackBar windows', 0, 255, lambda x: x)
cv2.setTrackbarPos('threshold', 'TrackBar windows', 127)
cv2.setTrackbarPos('maxValue', 'TrackBar windows', 255)

while cv2.waitKey(1) != ord('q'):
    thresh = cv2.getTrackbarPos('threshold', 'TrackBar windows')
    maxval = cv2.getTrackbarPos('maxValue', 'TrackBar windows')
    _, binary = cv2.threshold(src, thresh, maxval, cv2.THRESH_BINARY)
    binary_re = cv2.resize(binary, dsize=(0, 0), fx=0.7,
                           fy=0.7, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('TrackBar windows', binary_re)
cv2.destroyAllWindows()
