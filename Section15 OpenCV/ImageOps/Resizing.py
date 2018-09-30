import cv2

img1 = cv2.imread('kangaroos-rain-australia_71370_990x742.jpg', 1)
img2 = cv2.imread('Lighthouse.jpg', 1)
img3 = cv2.imread('Moon sinking, sun rising.jpg', 1)

resize_img1 = cv2.resize(img1, (100, 100))
resize_img2 = cv2.resize(img2, (100, 100))
resize_img3 = cv2.resize(img3, (100, 100))

cv2.imshow('res_kangaroos-rain-australia.jpg', resize_img1)
cv2.imshow('res_Lighthouse.jpg', resize_img2)
cv2.imshow('res_Moon sinking, sun rising.jpg', resize_img3)

cv2.imwrite('res_kangaroos.jpg', resize_img1)
cv2.imwrite('res_Lighthouse.jpg', resize_img2)
cv2.imwrite('res_Moon sinking, sun rising.jpg', resize_img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
# -------------------------------------------рациональный вариант-------------------------------------------------------------------------------

'''
import cv2
import glob               библиотека, с помощью которой можно создать контейнер и поместить в него файлы

images=glob.glob("*.jpg")  в параметры передаётся маска, по которой файлы отбираются в контейнер

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)

'''
