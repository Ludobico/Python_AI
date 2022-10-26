import cv2
import numpy as np

# 코너 검출
# 시-토마시 검출 : 해리스 코너 검출을 좀 더 개선한 알고리즘이다.
# 3차원 실수 행렬로 반환하며 n으로 코너점 검출 개수를 반환한다. x 좌표는 [i,0,0], y 좌표는 [i,0,1] 이다.
# 실수로 저장되므로 int로 변환하여 사용해야 한다.
# image: 입력이미지
# maxCorners : 최대 코너 개수, 코너 최댓값보다 낮은 개수만 반환, xCorners <=0 이면 무제한
# qualityLevel: 코너점 결정을 위한 값, 코너 품질은 0.0~1.0 사이의 값으로 할당할 수있으며 일반적으로 0.01~0.10 을 사용
# minDistance : 코너점 사이의 최소 거리, 설정된 최소 거리 이상의 값만 검출
# corners : 검출된 코너점 좌표
# mask : 마스크 이미지, 요소값이 0인 곳은 코너로 계산하지 않는다.
# blockSize : 코너 검출을 위한 블록 크기, 기본값은 3
# useHarrisDetector : 해리스 코너 방법 사용 여부, 기본값은 False
# k : 해리스 코너 검출 시 사용할 k 값

img = cv2.imread('./images/coffee.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 80, 0.01, 10)
corners = np.int32(corners)
