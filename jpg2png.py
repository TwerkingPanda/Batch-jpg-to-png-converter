from PIL import Image
import os
import sys
import pdb
input_path  = input("Enter the full path to the folder with JPEG files or place the program file with the image folder")
output_path = input("Enter the full path to the folder where the converted images are to be stored")
a=os.listdir(input_path)
os.chdir(input_path)
try:
	os.mkdir(output_path)
except:
	print("Failed to create the output directory. Make sure that the program has suffiecient rights/ try with another folder")
for i in a:
	if i[:-4] == '.jpg' :
		img = Image.open(i)	
		img.save(f'{output_path}/{i[:-4]}'+'.png')
