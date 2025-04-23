import cv2
import numpy as np
img = np.zeros((600, 600, 3), dtype=np.uint8)
cv2.circle(img, (300, 300), 200, (255, 255, 255), 4)
cv2.circle(img, (250, 250), 30, (255, 255, 255), 4)
cv2.circle(img, (350, 250), 30, (255, 255, 255), 4)
cv2.ellipse(img, (300,300), (100, 60), 0, 0, 180, (255, 255, 255), 4)
cv2.imshow("Human Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
