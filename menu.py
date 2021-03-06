import cv2
import numpy as np

x_start, y_start, x_end, y_end = 81, 168, 556, 338 

#size of one cell
x_one = (x_end - x_start)//5
y_one = (y_end - y_start)//3
y_end += y_one



def display_menu(img):
	#canvas #1 for display
	cv2.rectangle(img,(x_start, y_start - y_one -25),(x_end ,y_start -15),(0,255,0),3)
	#canvas #2 for digits
	cv2.rectangle(img,(x_start,y_start),(x_end,y_end),(0,255,0),3)

	#Vertical lines
	for i in range(1,5):
		cv2.line(img,(x_start + i*x_one, y_start),(x_start + i*x_one, y_end),(0,255,0),3)

	#Horizontal lines
	for i in range(1,4):
		cv2.line(img,(x_start, y_start + i*y_one),(x_end, y_start + i*y_one),(0,255,0),3)
	font = cv2.FONT_HERSHEY_SIMPLEX

	#Display digits
	fontsize, fontthickness = 1.5, 4
	#row #1
	cv2.putText(img,'1',(x_start + 0*x_one + (x_one//3),y_start + 1*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'2',(x_start + 1*x_one + (x_one//3),y_start + 1*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'3',(x_start + 2*x_one + (x_one//3),y_start + 1*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'+',(x_start + 3*x_one + (x_one//3),y_start + 1*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'-',(x_start + 4*x_one + (x_one//3),y_start + 1*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	#row #2
	cv2.putText(img,'4',(x_start + 0*x_one + (x_one//3),y_start + 2*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'5',(x_start + 1*x_one + (x_one//3),y_start + 2*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'6',(x_start + 2*x_one + (x_one//3),y_start + 2*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'X',(x_start + 3*x_one + (x_one//3),y_start + 2*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'/',(x_start + 4*x_one + (x_one//3),y_start + 2*y_one - 20), font, 1.1,(0,0,255),fontthickness,cv2.LINE_AA)
	#row #3
	cv2.putText(img,'7',(x_start + 0*x_one + (x_one//3),y_start + 3*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'8',(x_start + 1*x_one + (x_one//3),y_start + 3*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'9',(x_start + 2*x_one + (x_one//3),y_start + 3*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'0',(x_start + 3*x_one + (x_one//3),y_start + 3*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'.',(x_start + 4*x_one + (x_one//3),y_start + 3*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	#row #4
	cv2.putText(img,'C',(x_start + 0*x_one + (x_one//3),y_start + 4*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'<-',(x_start + 1*x_one + (x_one//3) - 10,y_start + 4*y_one - 10), font, 1.2,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'(',(x_start + 2*x_one + (x_one//3),y_start + 4*y_one - 15), font, 1,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,')',(x_start + 3*x_one + (x_one//3),y_start + 4*y_one - 15), font, 1,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.putText(img,'=',(x_start + 4*x_one + (x_one//3),y_start + 4*y_one - 10), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)

	return img