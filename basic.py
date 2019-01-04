#importing the packages
import cv2 
import numpy as np

#function to draw geometric shapes using open cv2 
def create_image():
	
		#creating window to draw
		img1 = np.zeros((512,512,3),np.uint8)
		
		#creating the shapes 
		cv2.line(img1,(0,99),(99,0),(255,0,0),2)
		cv2.rectangle(img1,(40,60),(80,70),(0,255,255),2)
		cv2.circle(img1,(60,60),10,(255,255,255),-1)
		cv2.ellipse(img1,(160,260),(50,20),0,0,360,(0,0,255),-1)
#      p = np.array([[80,2],[125,40],[179,19],[230,5],[30,50]],np.int32)
#	    p = p.reshape((1, 1 ,2))
#	    cv2.polylines(img1 , [p] , True , (255,255,0))

		#displaying the shapes on the window 
		cv2.imshow('Draw_line',img1)
		cv2.waitKey(0)
		cv2.destroyWindow('Draw_line')

#function to view Details of the image
def details(img): 
	print("Displaying the contents of the image\n",img)  
	print("Image type\t",type(img)) 
	print("datatype of the image\t",img.dtype)
	print("resolution of the image is\t",img.shape) 
	print("dimension of the image\t",img.ndim)
	print("Size of the image is\t",img.size)

def main():

	#specifying paths for reading and saving the files
	path = "C:/Users/puneet/Desktop/misc/4.1.01.tiff"
	output_path = "C:/Users/puneet/Desktop/4.1.01.jpeg"

	#reading the image using imread function
	img = cv2.imread(path,1)

	#creating a named window for capturing the image 
	cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)

	#displaying the image in the above window 
	cv2.imshow('Lena',img)

	#waiting of the window till any other key is pressed to destroy the window 
	k = cv2.waitKey(0)

	# wait for ESC key to exit
	if k == 27:         
    	#dstroying a particular window 
		cv2.destroyWindow('Lena')
 	
 	# wait for 's' key to save and exit
	elif k == ord('s'):
    		cv2.imwrite('new.png',img)
    		cv2.destroyWindow('Lena')
		
	
	create_image()

	val = input("Do you want to print the detailsof the image(Y/N)\n")
	if val=="Y":
		details(img)

if __name__ == '__main__':
                                                                                                                                     	
	main()   