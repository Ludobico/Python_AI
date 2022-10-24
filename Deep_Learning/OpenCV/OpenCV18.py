import cv2


# 흐림 효과
# 노이즈를 줄이거나 외부 영향을 최소화하는데 사용된다.
# 마치 초점이 맞지 않는 사진처럼 영상을 부드럽게 만드는 필터링 기법이다.

src = cv2.imread('./images/cat.jpg', cv2.IMREAD_COLOR)
for ksize in (3, 5, 6, 11, 15, 20, 25, 50, 100):
    dst = cv2.blur(src, (ksize, ksize), anchor=(-1, -1),
                   borderType=cv2.BORDER_DEFAULT)
    desc = 'mean: {}x{}'.format(ksize, ksize)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()
cv2.destroyAllWindows()
# src: 입력 이미지
# ksize: 가우시안 커널 크기
# sigmaX: x방향 sigma
# sigmaY: y방향 sigma
# borderType: 가장자리 픽셀 확장 방식
