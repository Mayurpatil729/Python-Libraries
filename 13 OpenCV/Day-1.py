import cv2

print(cv2.__version__)


# To Show Image
image = cv2.imread(filename="demo.jpg")
cv2.imshow("My Picture", image)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# # Image Shape : RGB
# image = cv2.imread(filename="demo.jpg")
# print(image.shape)
# cv2.imshow("My Picture", image)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()
