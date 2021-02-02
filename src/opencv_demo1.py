import numpy as np
import cv2


img_file = "opencv_study/img/hello.jpg" # 표시할 이미지 경로
save_file = 'opencv_study/img/hello_gray.jpg'
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)    # 이미지를 읽어서 img 변수에 할당

if img is not None:
  cv2.namedWindow('IMG', cv2.WINDOW_NORMAL)
  cv2.imshow('IMG', img)      # 읽은 이미지를 화면에 표시
  print(len(img))
  print(len(img[0]))
  cv2.waitKey()               # 키가 입력될 때 까지 대기 
  cv2.destroyAllWindows()     # 창 모두 닫기 
else:
    print('No image file.')
    