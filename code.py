#Import the necessary library
import cv2

#Load the first image
pic1=cv2.imread("Preetimam.jpg.jpeg")

#Crop a region of interest from the first image
pic2=pic1[95:245,95:235]

#Load the second image
pic3=cv2.imread("techguru.jpg.jpg")

#Replace a region in the second image with the cropped region from the first image
pic3[150:300,450:590]=pic2

#Display the modified image
cv2.imshow("photo",pic3)


cv2.waitKey()
cv2.destroyAllWindows()
