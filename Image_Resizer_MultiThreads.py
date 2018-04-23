import cv2
from multiprocessing import pool
from multiprocessing.dummy import Pool as ThreadPool
import sys
import os
import PIL
from PIL import Image

# This function loads a file, resize it and write in the output folder
def create_icon( inputFileName ):
	print(inputFileName, type(inputFileName))
	im = cv2.imread( inputFileName )
	print('image is read')
	small_im = cv2.resize( im, (224,224) )
	#small_im = cv2.resize(im, (0,0), fx=0.8, fy=0.8)
	print('image is resized')
	cv2.imwrite( 'out/'+inputFileName, small_im )
	print('image is written')

	# im = Image.open(inputFileName)
	# print('image is read')
	# im.thumbnail((224,224), Image.ANTIALIAS)
	# print('image is resized')
	# im.save('out/'+inputFileName,"JPEG")
	# print('image is written')





#fileList = 'images/annotations.txt'
 
# Load the list of images in the array lines
#imagesList = [line.rstrip('\n') for line in open(fileList)]
directory = sys.argv[1]
print(os.getcwd())
curr_dir =  os.path.join(os.getcwd(), directory )
print(curr_dir)

imagesList = []
for file_name in os.listdir(directory):
	imagesList.append(curr_dir + "/" + file_name)

print(imagesList)


# Create thread pool
pool = ThreadPool(4)
pool.map( create_icon, imagesList )