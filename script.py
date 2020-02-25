import cv2
img =cv2.imread("galaxy.jpg",0)
print(type(img))
print(img)
resized_image=cv2.resize(img,(img.shape[1]/2))
cv2.imshow("G",img)
cv2.waitKey(0)
