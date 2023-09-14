import numpy as np
import cv2

lower_arr=np.array([[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]])
higher_arr=np.array([[0.0, -1.0, 0.0],[-1.0, 4.0, -1.0],[0.0, -1.0, 0.0]])
sharp_arr=np.array([[-1.0, -1.0, -1.0],[-1.0, 9.0, -1.0],[-1.0, -1.0, -1.0]])

for i in range(1,6):
  img_src = cv2.imread("1.jpg")
  
  kernel_lower = lower_arr/(np.sum(lower_arr) if np.sum(lower_arr)!=0 else 1)
  kernel_higher = higher_arr/(np.sum(higher_arr) if np.sum(higher_arr)!=0 else 1)
  kernel_sharp = sharp_arr/(np.sum(sharp_arr) if np.sum(higher_arr)!=0 else 1)

  img_lower_rst = cv2.filter2D(img_src,-1,kernel_lower)
  img_higher_rst = cv2.filter2D(img_src,-1,kernel_higher)
  img_sharp = cv2.filter2D(img_src,-1,kernel_sharp)

  result_image = np.concatenate((img_lower_rst, img_higher_rst, img_sharp), axis=1)

  cv2.imshow("Result", result_image)