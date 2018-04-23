import os
import pandas as pd

#data = pd.read_csv("sample.csv")

directory = os.getcwd()
print(directory)

directory1 = os.getcwd() + '/checked'
imagesList1 = []
for file_name in os.listdir(directory1):
	imagesList1.append(file_name)

print(imagesList1)
imagesList1 = imagesList1[1:]
print(imagesList1)


directory2 = os.getcwd() + '/Polka'
imagesList2 = []
for file_name in os.listdir(directory2):
	imagesList2.append(file_name)
	
print(imagesList2)
imagesList2 = imagesList2[1:]
print(imagesList2)

directory3 = os.getcwd() + '/Camouflage'
imagesList3 = []
for file_name in os.listdir(directory3):
	imagesList3.append(file_name)
	
print(imagesList3)
imagesList3 = imagesList3[1:]
print(imagesList3)



directory = os.getcwd() + '/SMOTE_train'

imagesList = []
cnt = 0
for file_name in os.listdir(directory):
	if cnt < 67087:
		imagesList.append(file_name)
	cnt += 1

print(imagesList)
imagesList = imagesList[1:]
print(imagesList)



f = open("Newdata_labels.csv", "w")
f.write("id" + "," + "class" + "\n")

for image in imagesList1:
	class_name = image.split('_')[0]
	class_name = class_name.replace(" ", "_")
	print(image + "," + class_name)
	f.write(image + "," + class_name + "\n")

for image in imagesList2:
	class_name = image.split('_')[0]
	class_name = class_name.replace(" ", "_")
	print(image + "," + class_name)
	f.write(image + "," + class_name + "\n")

class_name = 'Polka_Dots'
for image in imagesList3:
	print(image + "," + class_name)
	f.write(image + "," + class_name + "\n")

for image in imagesList:
	class_name = image.split('_')[1]
	class_name = class_name.replace(" ", "_")
	print(image + "," + class_name)
	f.write(image + "," + class_name + "\n")

f.close()