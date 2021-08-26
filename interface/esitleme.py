import cv2

path1 = "./emre.jpeg"
path2 = "C:/Users/ayper/Desktop/ise_giris/Evraklar/Vesikalık.png"

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
a, b, c = img1.shape
print(a, b)
img2 = cv2.resize(img2, (a,b))

cv2.imwrite("./semih2.jpg", img2)