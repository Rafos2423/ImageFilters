import numpy as np
import cv2

for i in range(1,6):
  orig_img = cv2.imread(f"2\\durty_images\\{i}.jpg")

  filter_img = cv2.medianBlur(orig_img,3)

  result_image = np.concatenate((orig_img, filter_img), axis=1)
  cv2.imshow("Result", result_image)
  cv2.waitKey(0)