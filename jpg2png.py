from PIL import Image
import os
import sys
import pdb
input_path  = input("Enter the full path to the folder with JPEG files or place the program file with the image folder:\n")
output_path = 
a=os.listdir(input_path)
os.chdir(input_path)
output_path = "/PNGimages"
try:
	os.mkdir(output_path)
except:
	print("Failed to create the output directory. Most likely, you do not have access to create directories at this location")
	try:
		output_path = input("Enter full path of where you want to save your converted images:\n")
	except:
		print("Failed to create the output directory. Most likely, you do not have access to create directories at this location")
for i in a:
	if i[-4:] == '.jpg' :
		img = Image.open(i)	
		img.save(f'{output_path}/{i[:-4]}'+'.png')
